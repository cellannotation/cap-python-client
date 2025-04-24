from typing import List, Dict, Literal
import time
import http.client
import json
import jwt
import os
from uuid import uuid4
import pandas as pd
import httpx

from .client.client import _Client
from .client.input_types import (
    DatasetSearchOptions,
    LookupDatasetsFiltersInput,
    LookupDatasetsSearchInput,
    SearchByMetadataArgs,
    DatasetSearchSort,
    CellLabelsSearchOptions,
    LookupLabelsFilters,
    LookupCellsSearch,
    SearchLabelByMetadataArgs,
    CellLabelsSearchSort,
    GetDatasetEmbeddingDataInput,
    GetGeneralDiffInput,
    GetHighlyVariableGenesInput,
    PostSaveEmbeddingSessionInput,
    PostHeatmapInput
)
from .client.embedding_data import EmbeddingDataDatasetEmbeddingData
from .client.heatmap import HeatmapDatasetEmbeddingDiffHeatMap

CAP_API_URL = "https://celltype.info/graphql"
CAP_AUTHENTICATE_URL = "us-central1-capv2-gke-prod.cloudfunctions.net" # https://${var.gcp_region}-${var.gcp_project_id}.cloudfunctions.net/authenticate-token

SESSION_ID = str
DIFF_KEY = str
SELECTION_KEY = str
CELL_LABELS_MODE = "cell-labels"


class MDSession:
    def __init__(self, dataset_id: str, _client: _Client):
        self.__client: _Client = _client
        self._dataset_id: str = dataset_id
        self._session_id: str = None
        self._dataset_snapshot = None
        self._embeddings: list[str] = None
        self._labelsets: list[str] = None
        self._clusterings: list[str] = None
        self._metadata: list[str] = None
    
    def __repr__(self) -> str:
        return f"Molecular Data page session for dataset id: {self.dataset_id}"
    
    def __str__(self) -> str:
        return self.__repr__()
    
    @property
    def dataset_id(self) -> str:
        return self._dataset_id
    
    @property
    def dataset_snapshot(self):
        return self._dataset_snapshot
    
    @property
    def embeddings(self) -> list[str]:
        return self._embeddings
    
    @property
    def clusterings(self) -> list[str]:
        return self._clusterings
    
    @property
    def labelsets(self) -> list[str]:
        return self._labelsets
    
    @property
    def session_id(self) -> str:
        return self._session_id

    def _check_md_ready(self):
        ready = self.__client.dataset_ready(self.dataset_id)
        if not ready.dataset.is_embeddings_up_to_date:
            raise RuntimeError(f"The Molecular Data for the dataset {self.dataset_id} is not ready!")
        
    def _get_clusterings(self) -> list[str]:
        res = self.__client.cluster_types(self.dataset_id)
        res = res.dataset
        clusters = res.embedding_cluster_types
        cluster_names = [cl.name for cl in clusters]
        return cluster_names
    
    def _get_embeddings(self) -> list[str]:
        res = self.__client.md_commons_query(self.dataset_id)
        res = res.dataset
        embeddings = res.embeddings
        emb_names = [e.name for e in embeddings]
        return emb_names

    def _get_cell_type_labelsets(self) -> list[str]:
        if self.dataset_snapshot is None:
            raise RuntimeError("The dataset snapshot is not ready, call MDSession.create_session first!")
        
        labelsets = []
        for lbst in self.dataset_snapshot.labelsets:
            if lbst.mode == CELL_LABELS_MODE:
                labelsets.append(lbst.name)
        return labelsets

    def create_session(
            self,
        ) -> SESSION_ID:
        """
        Creates a new session for embedding processing.

        This method performs a sanity check, retrieves the initial state of the dataset, 
        fetches clusterings and embeddings, and then initializes a new session with a 
        unique session ID. The session information is saved via the client.

        Returns:
            str: The unique session ID of the newly created embedding session.
        """

        self._check_md_ready()

        ds = self.__client.dataset_initial_state_query(self.dataset_id)
        self._dataset_snapshot = ds.dataset
        self._clusterings = self._get_clusterings()
        self._embeddings = self._get_embeddings()
        self._labelsets = self._get_cell_type_labelsets()

        session_id = str(uuid4())
 
        data = PostSaveEmbeddingSessionInput(
            session_id = session_id,
            dataset = self._dataset_snapshot.model_dump()
        )
        response = self.__client.create_session(
            data = data
        )
        self._dataset_snapshot = response.save_embedding_session
        self._session_id = session_id
        return self.session_id
    
    def embedding_data(
            self, 
            embedding: str,
            max_points: int,
            labelsets: List[str] = None,
            selection_gene: str = None,
            selection_key_major: str = None,
            selection_key_minor: str = None,
        ) -> EmbeddingDataDatasetEmbeddingData:
        """
        Retrieves embedding data for the specified embedding type, with optional filtering and downsampling.

        Parameters:
        -----------
        embedding : str
            The name of the embedding to retrieve. Must be present in `self.embeddings`.
        max_points : int
            The maximum number of points to include in the response. Data may be downsampled to meet this limit.
        labelsets : List[str], optional
            A list of label sets to include in the embedding data. Defaults to None.
        selection_gene : str, optional
            If provided, returns a list of expression values for the specified gene. Defaults to None.
        selection_key_major : str, optional
            If provided, returns a list of boolean markers indicating whether each point is within the major selection. Defaults to None.
        selection_key_minor : str, optional
            If provided, returns a list of boolean markers indicating whether each point is within the minor selection. Defaults to None.

        Returns:
        --------
        EmbeddingDataDatasetEmbeddingData
            An object containing the embedding data, including observation IDs, selections, embeddings, annotations, 
            and gene expression values.

        Raises:
        -------
        ValueError
            If the specified embedding is not found in `self.embeddings`.
        """

        if embedding not in self.embeddings:
            raise ValueError(f"Embedding '{embedding}' is not found in the list of '{self.embeddings}'")
        
        options =  GetDatasetEmbeddingDataInput(
            embedding = embedding,
            scale_max_plan = max_points,
            session_id = self.session_id,
            labelsets = labelsets,
            selection_gene = selection_gene,
            selection_key_major = selection_key_major,
            selection_key_minor = selection_key_minor,
        )
        
        # TODO: is not workgin with new rc1
        # update request later https://capdevelopment.atlassian.net/browse/MVP-6489
        response = self.__client.embedding_data(
            dataset_id = self.dataset_id,
            options = options
        )
        data = response.dataset.embedding_data
        return data

    def _labelset_id_from_name(self, labelset_name) -> str:
        if self.dataset_snapshot is None:
            raise RuntimeError("Dataset snapshot is not ready, create session first!")
        
        for lbst in self.dataset_snapshot.labelsets:
            if lbst.name == labelset_name:
                return lbst.id
        
        raise ValueError(f"Can't find labelset '{labelset_name}' in dataset snapshot!")

    def general_de(
            self, 
            labelset: str,
            random_seed: int = 42,
        ) -> DIFF_KEY:
        """
        Performs a general differential expression (DE) analysis.

        This method conducts a differential expression analysis, comparing each of the 
        top 10 largest labels within the specified label set against all other data points.

        Parameters:
        -----------
        labelset : str
            The name of the label set to use for differential expression analysis. 
            Must be present in `self.labelsets`.
        random_seed : int, optional
            The random seed for reproducibility. Defaults to 42.

        Returns:
        --------
        DIFF_KEY
            A string key associated with the results of the differential expression analysis.

        Raises:
        -------
        ValueError
            If the specified label set is not found in `self.labelsets`.
        """
        if labelset not in self.labelsets:
            raise ValueError(f"Labelset '{labelset}' is not found in the list of '{self.labelsets}'")
        
        labelset_id = self._labelset_id_from_name(labelset)

        options = GetGeneralDiffInput(
            random_seed = random_seed,
            session_id = self.session_id,
            labelset_id = labelset_id
        )
        response = self.__client.general_de(
            dataset_id = self.dataset_id,
            options = options,
        )
        diff_key = response.dataset.general_diff
        return diff_key
    
    def highly_variable_genes(
            self,
            gene_name_filter: str = None,
            pseudogenes_filter: bool = True,
            offset: int = 0,
            limit: int = 50,
            sort_order: Literal["desc", "asc"] = "desc"
        ) -> pd.DataFrame:
        """
        Retrieves a list of highly variable genes from the specified dataset.

        This method queries the dataset for highly variable genes based on dispersion values.
        It supports filtering by gene name, excluding pseudogenes, and sorting the results.
        The retrieved genes are returned as a Pandas DataFrame with columns for gene names
        and their respective dispersion values.

        Args:
            dataset_id (str): The unique identifier of the dataset.
            gene_name_filter (str, optional): A filter to include only genes matching a given prefix.
            pseudogenes_filter (bool, optional): If True, filters out genes which are often
                over-expressed but biologically non-informative. Defaults to True.
                See https://github.com/cellannotation/cap-gene-filtering for details.
            offset (int, optional): The starting index for pagination. Defaults to 0.
            limit (int, optional): The maximum number of genes to return. Defaults to 50.
            sort_order (Literal["desc", "asc"], optional): The sorting order for dispersion values.
                Defaults to "desc" (descending).

        Returns:
            pd.DataFrame: A DataFrame containing highly variable genes with two columns:
                - "gene_symbol" (str): The gene symbol.
                - "dispersion" (float): The dispersion value of the gene. Initially, the gene
                    dispersion values are calculated over the log-transformed count matrix,
                    these dispersion values are then log-transformed again before being displayed
                    in the gene table.
        """
 
        options = GetHighlyVariableGenesInput(
            offset = offset,
            limit = limit,
            gene_name_filter = gene_name_filter,
            use_genes_pattern = pseudogenes_filter,
            sort_by = "dispersion",
            sort_order = sort_order
        )
        res = self.__client.highly_variable_genes(
            dataset_id = self.dataset_id,
            options = options
        )
        hvg_list = res.dataset.embedding_highly_variable_genes
        
        df = pd.DataFrame({
            "gene_symbol": [g.name for g in hvg_list],
            "dispersion": [g.dispersion for g in hvg_list],
        })
        return df

    def is_md_cache_ready(self) -> bool:
        """
        Checks whether the molecular data cache is ready.

        This method queries the dataset's file status and determines if the 
        molecular data page files are fully prepared and available.

        Returns:
        --------
        bool
            True if the metadata cache is ready, otherwise False.
        """
        res = self.__client.files_status(self.dataset_id)
        status = res.dataset.get_md_files_status
        return status == "ready"

    def heatmap(
            self,
            diff_key: DIFF_KEY,
            n_top_genes: int = 3,
            max_cells_displayed: int = 1000,
            gene_name_filter: str = None,
            pseudogenes_filter: bool = True,
            selection_key: SELECTION_KEY = None,
            include_reference: bool = True
        ) -> HeatmapDatasetEmbeddingDiffHeatMap:
        
        options=PostHeatmapInput(
            diff_key = diff_key,
            n_genes = n_top_genes,
            scale_max_plan = max_cells_displayed,
            genes_filter = gene_name_filter,
            use_genes_pattern = pseudogenes_filter,
            session_id = self.session_id,
            include_reference_selection = include_reference,
            selection_key = selection_key,
        )

        # TODO: update api, it was changed on rc1 https://capdevelopment.atlassian.net/browse/MVP-6489
        res = self.__client.heatmap(
            dataset_id=self.dataset_id,
            options=options,
        )
        heatmap = res.dataset.embedding_diff_heat_map
        return heatmap


class CapClient:
    def __init__(
            self,
            url: str = CAP_API_URL, 
            auth_url: str = CAP_AUTHENTICATE_URL,
            login: str = None,
            pwd: str = None,
            custom_token: str = None  
        ) -> None:
        headers = None
        client = httpx.Client(timeout=300, headers=headers)
        self.__client = _Client(url, headers=headers, http_client=client)
        self._login = login if login is not None else os.environ.get('CAP_LOGIN')
        self._pwd = pwd if pwd is not None else os.environ.get('CAP_PWD')
        self._custom_token = custom_token if custom_token is not None else os.environ.get('CAP_TOKEN')
        self._token: str = None
        self._token_expiry_time: time = None
        self._error_status: str = None
        self.auth_url = auth_url

    def _auth_request (
            self,
            base_url: str, 
            url: str,
            body: dict
        ) -> bool: 
        connection = http.client.HTTPSConnection(base_url)
        headers = {'Content-type': 'application/json'}
        connection.request("POST", url = url,  body=json.dumps(body), headers=headers)
        response = connection.getresponse()
        if (response.status == 200):
            try:
                response = response.read().decode()
                self._token = json.loads(response)['idToken']
                # TODO : Add signature verification https://capdevelopment.atlassian.net/browse/MVP-6392
                self._token_expiry_time = jwt.decode(self._token, options={"verify_signature": False})['exp']
                self._error_status = None
                return True
            except: # TODO: implement appropriate error handling https://capdevelopment.atlassian.net/browse/MVP-6489
                self._error_status = "Failed to parse 200 OK response to get ID token"
                return False
        self._error_status = "Failed to get ID token " + response.reason 
        return False
    
    def authenticate(
        self
     ) -> bool:
        # try authenticate by custom token first
        if self._custom_token is not None:
            body = {'token':self._custom_token}
            if (self._auth_request(base_url= self.auth_url, url = "/authenticate-token", body = body)):
                return True
        if self._login is not None and self._pwd is not None:    
            body = {'email':self._login, 'password': self._pwd}
            if (self._auth_request(base_url = self.auth_url, url = "/authenticate-user", body = body)):
                return True
        self._error_status = "Missing CAP client authetication settings. Check CAP_LOGIN, CAP_PWD or CAP_TOKEN enviroment variables."
        return False

    @property     
    def error_status(self) -> str:
        return self._error_status
    
    @property
    def id_token(self) -> str:
        return self._token
    
    @property
    def token_expiry_time(self) -> time:
        return self._token_expiry_time

    def search_datasets(
        self,
        search: List[str] = None,
        organism: List[str] = None,
        tissue: List[str] = None,
        assay: List[str] = None,
        limit: int = 50,
        offset: int = 0,
        sort: List[Dict[str, str]] = [],
    ) -> pd.DataFrame:
        sorting = []
        for item in sort:
            key = list(item.keys())[0]
            value = list(item.values())[0]
            sorting.append(DatasetSearchSort(field=key, order=value))
        search_options = DatasetSearchOptions(limit=limit, offset=offset, sort=sorting)

        metadata = []
        if organism:
            metadata.append(SearchByMetadataArgs(field="organism", values=organism))
        if tissue:
            metadata.append(SearchByMetadataArgs(field="tissue", values=tissue))
        if assay:
            metadata.append(SearchByMetadataArgs(field="assay", values=assay))

        search_filter = LookupDatasetsFiltersInput(metadata=metadata)
        search_input = None
        if search:
            search_input = LookupDatasetsSearchInput(name=search)

        response = self.__client.search_datasets(
            options=search_options, filter=search_filter, search=search_input
        )
        df = pd.DataFrame([r.model_dump() for r in response.results])        
        return df

    def search_cell_labels(
        self,
        search: str = None,
        organism: List[str] = None,
        tissue: List[str] = None,
        assay: List[str] = None,
        limit: int = 50,
        offset: int = 0,
        sort: List[Dict[str, str]] = [],
    ) -> pd.DataFrame:
        sorting = []
        for item in sort:
            key = list(item.keys())[0]
            value = list(item.values())[0]
            sorting.append(CellLabelsSearchSort(field=key, order=value))
        search_options = CellLabelsSearchOptions(
            limit=limit, offset=offset, sort=sorting
        )

        metadata = []
        if organism:
            metadata.append(
                SearchLabelByMetadataArgs(field="organism", values=organism)
            )
        if tissue:
            metadata.append(SearchLabelByMetadataArgs(field="tissue", values=tissue))
        if assay:
            metadata.append(SearchLabelByMetadataArgs(field="assay", values=assay))

        search_filter = LookupLabelsFilters(metadata=metadata)
        search_input = None
        if search:
            search_input = LookupCellsSearch(name=search)

        response = self.__client.lookup_cells(
            options=search_options, filter=search_filter, search=search_input
        )
        df = pd.DataFrame([lc.model_dump() for lc in response.lookup_cells])        
        return df

    def md_session(self, dataset_id: str) -> MDSession:
        return MDSession(dataset_id=dataset_id, _client=self.__client)
