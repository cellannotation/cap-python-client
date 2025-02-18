from typing import List, Dict
import time
import http.client
import json
import jwt
import os

from .client.client import Client
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
    GetDatasetClustersDataInput,
    GetDatasetEmbeddingDataInput,
    GetGeneralDiffInput,
    PostHeatmapInput,
    GetHighlyVariableGenesInput,
    PostSaveEmbeddingSessionInput,
    DatasetObjectInput
)
from .client.search_datasets import SearchDatasets
from .client.lookup_cells import LookupCells
from .client.download_urls import DownloadUrls
from .client.embedding_clusters import EmbeddingClusters
from .client.embedding_data import EmbeddingData
from .client.general_de import GeneralDE
from .client.heatmap import Heatmap
from .client.highly_variable_genes import HighlyVariableGenes
from .client.create_session import CreateSession


CAP_API_URL = "https://celltype.info/graphql"
CAP_AUTHENTICATE_URL = "us-central1-capv2-gke-prod.cloudfunctions.net" # https://${var.gcp_region}-${var.gcp_project_id}.cloudfunctions.net/authenticate-token
class Cap(Client):
    def __init__(
            self, 
            url: str = CAP_API_URL, 
            auth_url: str = CAP_AUTHENTICATE_URL,
            login: str = None,
            pwd: str = None,
            custom_token: str = None  
        ) -> None:
        super().__init__(url)
        self._login = login if login is not None else os.environ.get('CAP_LOGIN')
        self._pwd = pwd if pwd is not None else os.environ.get('CAP_PWD')
        self._custom_token = custom_token if custom_token is not None else os.environ.get('CAP_TOKEN')
        self._token: str = None
        self._token_expiry_time: time = None
        self._error_status: str = None
        self.auth_url = auth_url

    def _request (
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
                # TODO : Add signature verification 
                self._token_expiry_time = jwt.decode(self._token, options={"verify_signature": False})['exp']
                self._error_status = None
                return True
            except: 
                self._error_status = "Failed to parse 200 OK response to get ID token"
                return False  
        self._error_status = "Failed to get ID token " + response.reason 
        return False
    
    def _authenticate(
        self
     ) -> bool:
        # try authenticate by custom token first
        if self._custom_token is not None:
            body = {'token':self._custom_token}
            if (self._request(base_url= self.auth_url, url = "/authenticate-token", body = body)):
                return True
        if self._login is not None and self._pwd is not None:    
            body = {'email':self._login, 'password': self._pwd}
            if (self._request(base_url = self.auth_url, url = "/authenticate-user", body = body)):
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
    ) -> SearchDatasets:
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

        response = super().search_datasets(
            options=search_options, filter=search_filter, search=search_input
        )
        return response

    def search_datasets_json(
        self,
        search: List[str] = None,
        organism: List[str] = None,
        tissue: List[str] = None,
        assay: List[str] = None,
        limit: int = 50,
        offset: int = 0,
        sort: List[Dict[str, str]] = []
    ) -> str:
        response = self.search_datasets(
            search,
            organism,
            tissue,
            assay,
            limit,
            offset,
            sort
        )
        return response.model_dump_json()

    def search_cell_labels(
        self,
        search: List[str] = None,
        organism: List[str] = None,
        tissue: List[str] = None,
        assay: List[str] = None,
        limit: int = 50,
        offset: int = 0,
        sort: List[Dict[str, str]] = [],
    ) -> LookupCells:
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

        response = super().lookup_cells(
            options=search_options, filter=search_filter, search=search_input
        )
        return response
    
    def search_cell_labels_json(
        self,
        search: List[str] = None,
        organism: List[str] = None,
        tissue: List[str] = None,
        assay: List[str] = None,
        limit: int = 50,
        offset: int = 0,
        sort: List[Dict[str, str]] = [],
    ) -> str:
        response = self.search_cell_labels(
            self,
            search,
            organism,
            tissue,
            assay,
            limit,
            offset,
            sort
        )
        return response.model_dump_json()
    
    def download_urls_json(self, dataset_id: str) -> str:
        response = super().download_urls(dataset_id)
        return response.model_dump_json()
    
    def files_status_json(self, dataset_id: str) -> str:
        response = super().files_status(dataset_id)
        return response.model_dump_json()
    
    def md_commons_query_json(self, dataset_id: str) -> str:
        response = super().md_commons_query(dataset_id)
        return response.model_dump_json()
    
    def dataset_initial_state_query_json(self, dataset_id: str) -> str:
        response = super().dataset_initial_state_query(dataset_id)
        return response.model_dump_json()
    
    def cluster_types_json(self, dataset_id: str) -> str:
        response = super().cluster_types(dataset_id)
        return response.model_dump_json()
    
    def dataset_ready_json(self, dataset_id: str) -> str:
        response = super().dataset_ready(dataset_id)
        return response.model_dump_json()
    
    def md_ready_json(self, dataset_id: str) -> str:
        response = super().md_ready(dataset_id)
        return response.model_dump_json()
    
    def embeddings_clusters(
            self, 
            dataset_id: str, 
            cluster: str
        ) -> EmbeddingClusters:

        response = super().embedding_clusters(
            dataset_id = dataset_id, 
            cluster = GetDatasetClustersDataInput(cluster)
        )
        return response
    
    def embeddings_clusters_json(
            self, 
            dataset_id: str, 
            cluster: str
        ) -> str:

        response = self.embedding_clusters(
            dataset_id = dataset_id, 
            cluster = GetDatasetClustersDataInput(cluster) 
        )
        return response.model_dump_json()

    def embedding_data(
            self, 
            dataset_id: str,
            embedding: str,
            scale_max_plan: float,
            session_id: str = None,
            labelsets: List[str] = None,
            selection_gene: str = None,
            selection_key_major: str = None,
            selection_key_minor: str = None
        ) -> EmbeddingData:
 
        options = GetDatasetEmbeddingDataInput(
            embedding = embedding,
            selection_gene = selection_gene,
            scale_max_plan = scale_max_plan,
            selection_key_major = selection_key_major,
            selection_key_minor = selection_key_minor,
            session_id = session_id,
            labelsets = labelsets
        )
        response = super().embedding_data(
            dataset_id = dataset_id,
            options = options
        )
        return response
    
    def embedding_data_json(
            self, 
            dataset_id: str,
            embedding: str,
            scale_max_plan: float,
            session_id: str = None,
            labelsets: List[str] = None,
            selection_gene: str = None,
            selection_key_major: str = None,
            selection_key_minor: str = None
        ) -> str:
 
        response = self.embedding_data(
            dataset_id = dataset_id,
            embedding = embedding,
            scale_max_plan = scale_max_plan,
            session_id = session_id,
            labelsets = labelsets,
            selection_gene = selection_gene,
            selection_key_major = selection_key_major,
            selection_key_minor = selection_key_minor
        )
        return response.model_dump_json()
    
    def general_de(
            self, 
            dataset_id: str,
            labelset_id: str,
            random_seed: float = 123,
            session_id: str = None
        ) -> GeneralDE:
 
        options = GetGeneralDiffInput(
            random_seed = random_seed,
            session_id = session_id,
            labelset_id = labelset_id
        )
        response = super().general_de(
            dataset_id = dataset_id,
            options = options
        )
        return response

    def general_de_json(
            self, 
            dataset_id: str,
            labelset_id: str,
            random_seed: float = 123,
            session_id: str = None
        ) -> GeneralDE:
 
        response = self.general_de(
            dataset_id = dataset_id,
            labelset_id = labelset_id,
            random_seed = random_seed,
            session_id = session_id
        )
        return response.model_dump_json()
    
    def heatmap(
            self, 
            dataset_id: str,
            diff_key: str,
            n_genes: int = None,
            scale_max_plan: float = None,
            genes_filter: List[str] = None,
            use_genes_pattern: bool = None,
            session_id: str = None,
            include_reference_selection: bool = None,
            selection_key: str = None
        ) -> Heatmap:
 
        options = PostHeatmapInput(
            diff_key = diff_key,
            n_genes = n_genes,
            scale_max_plan = scale_max_plan,
            genes_filter = genes_filter,
            use_genes_pattern = use_genes_pattern,
            session_id = session_id,
            include_reference_selection = include_reference_selection,
            selection_key = selection_key
        )
        response = super().heatmap(
            dataset_id = dataset_id,
            options = options
        )
        return response

    def heatmap_json(
            self, 
            dataset_id: str,
            diff_key: str,
            n_genes: int = None,
            scale_max_plan: float = None,
            genes_filter: List[str] = None,
            use_genes_pattern: bool = None,
            session_id: str = None,
            include_reference_selection: bool = None,
            selection_key: str = None
        ) -> Heatmap:
 
        response = self.heatmap(
            dataset_id = dataset_id,
            diff_key = diff_key,
            n_genes = n_genes,
            scale_max_plan = scale_max_plan,
            genes_filter = genes_filter,
            use_genes_pattern = use_genes_pattern,
            session_id = session_id,
            include_reference_selection = include_reference_selection,
            selection_key = selection_key
        )
        
        return response.model_dump_json()
    
    def highly_variable_genes(
            self, 
            dataset_id: str,
            offset: float,
            limit: float,
            gene_name_filter: str = None,
            use_genes_pattern:bool = None,
            sort_by: str = None,
            sort_order:str = None
        ) -> HighlyVariableGenes:
 
        options = GetHighlyVariableGenesInput(
            offset = offset,
            limit = limit,
            gene_name_filter = gene_name_filter,
            use_genes_pattern = use_genes_pattern,
            sort_by = sort_by,
            sort_order = sort_order
        )
        response = super().highly_variable_genes(
            dataset_id = dataset_id,
            options = options
        )
        return response
    
    def highly_variable_genes_json(
            self, 
            dataset_id: str,
            offset: float,
            limit: float,
            gene_name_filter: str = None,
            use_genes_pattern:bool = None,
            sort_by: str = None,
            sort_order:str = None
        ) -> HighlyVariableGenes:
 
        response = self.highly_variable_genes(
            dataset_id = dataset_id,
            offset = offset,
            limit = limit,
            gene_name_filter = gene_name_filter,
            use_genes_pattern = use_genes_pattern,
            sort_by = sort_by,
            sort_order = sort_order
        )
    
        return response.model_dump_json()
    
    def create_session(
            self, 
            session_id: str,
            dataset: DatasetObjectInput
        ) -> CreateSession:
 
        data = PostSaveEmbeddingSessionInput(
            session_id = session_id,
            dataset = dataset
        )
        response = super().create_session(
            data = data
        )
        return response
    
    def create_session_json(
            self, 
            session_id: str,
            dataset: dict = None
        ) -> CreateSession:
 
        response = self.create_session(
            session_id = session_id,
            dataset = dataset
        )
        
        return response.model_dump_json()
    