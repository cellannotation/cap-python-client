from typing import List, Dict
import time
import http.client
import json
import jwt
import os
from uuid import uuid4

from client.client import _Client
from client.input_types import (
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
    DatasetObjectInput
)
from client.search_datasets import SearchDatasets
from client.lookup_cells import LookupCells
from client.embedding_data import EmbeddingData
from client.general_de import GeneralDE
from client.highly_variable_genes import HighlyVariableGenes
from client.create_session import CreateSession


CAP_API_URL = "https://celltype.info/graphql"
CAP_AUTHENTICATE_URL = "us-central1-capv2-gke-prod.cloudfunctions.net" # https://${var.gcp_region}-${var.gcp_project_id}.cloudfunctions.net/authenticate-token


class MDSession:
    def __init__(self, dataset_id: str, _client: _Client):
        self.__client: _Client = _client
        self._dataset_id: str = dataset_id
        self._session_id: str = None
        self._dataset_shapshot = None
        self._embeddings: list[str] = None
        self._labelsets: list[str] = None
        self._clusterings: list[str] = None
        self._metadata: list[str] = None
    
    def __repr__(self) -> str:
        return f"Molecular Data page session for dataset id: {self.dataset_id}"
    
    def _sanity_check(self):
        ready = self.__client.dataset_ready(self.dataset_id)
        if not ready.dataset.is_embeddings_up_to_date:
            raise RuntimeError(f"The Molecular Data for the dataset {self.dataset_id} is not ready!")
        ds = self.__client.dataset_initial_state_query(self.dataset_id)
        self._dataset_shapshot = ds.dataset
        self._session_id = self.__client.create_session(data=self._dataset_shapshot)

    @property
    def dataset_id(self):
        return self._dataset_id
   
    def embedding_data(
            self, 
            embedding: str,
            scale_max_plan: float,
            session_id: str = None,
            labelsets: List[str] = None,
            selection_gene: str = None,
            selection_key_major: str = None,
            selection_key_minor: str = None,
        ) -> EmbeddingData:
        """
        # TODO: fill
        """

        # TODO: validate embeddings
        
        options =  GetDatasetEmbeddingDataInput(
            embedding = embedding,
            selection_gene = selection_gene,
            scale_max_plan = scale_max_plan,
            selection_key_major = selection_key_major,
            selection_key_minor = selection_key_minor,
            session_id = session_id,
            labelsets = labelsets
        )

        response = self.__client.embedding_data(
            dataset_id = self.dataset_id,
            options = options
        )
        return response
        
    def general_de(
            self, 
            dataset_id: str,
            labelset_id: str,
            random_seed: float = 123,
            session_id: str = None
        ) -> GeneralDE:
        """
        # TODO: fill
        """
 
        options = GetGeneralDiffInput(
            random_seed = random_seed,
            session_id = session_id,
            labelset_id = labelset_id
        )
        response = self.__client.general_de(
            dataset_id = dataset_id,
            options = options
        )
        return response
    
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
        """
        # TODO: fill
        """
 
        options = GetHighlyVariableGenesInput(
            offset = offset,
            limit = limit,
            gene_name_filter = gene_name_filter,
            use_genes_pattern = use_genes_pattern,
            sort_by = sort_by,
            sort_order = sort_order
        )
        response = self.__client.highly_variable_genes(
            dataset_id = dataset_id,
            options = options
        )
        return response
        
    def create_session(
            self,
        ) -> CreateSession:
        """
        # TODO: fill
        """

        self._sanity_check()
        session_id = uuid4()
 
        data = PostSaveEmbeddingSessionInput(
            session_id = session_id,
            dataset = self._dataset_shapshot
        )
        response = self.__client.create_session(
            data = data
        )
        self._session_id = session_id
        return response


class CapClient:
    def __init__(
            self,
            url: str = CAP_API_URL, 
            auth_url: str = CAP_AUTHENTICATE_URL,
            login: str = None,
            pwd: str = None,
            custom_token: str = None  
        ) -> None:
        self.__client = _Client(url)
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
                # TODO : Add signature verification 
                self._token_expiry_time = jwt.decode(self._token, options={"verify_signature": False})['exp']
                self._error_status = None
                return True
            except: 
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

        response = self.__client.search_datasets(
            options=search_options, filter=search_filter, search=search_input
        )
        return response

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

        response = self.__client.lookup_cells(
            options=search_options, filter=search_filter, search=search_input
        )
        return response
    
    def open_md_session(self, dataset_id: str) -> MDSession:
        return MDSession(dataset_id=dataset_id, _client=self.__client)


if __name__ ==  "__main__":
    cap = CapClient()
    md = cap.open_md_session("825")
    sid = md.create_session()

    print(sid)
    