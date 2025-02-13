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
    GetDatasetEmbeddingDataInput
)
from .client.search_datasets import SearchDatasets
from .client.lookup_cells import LookupCells
from .client.download_urls import DownloadUrls
from .client.embedding_clusters import EmbeddingClusters
from .client.embedding_data import EmbeddingData

CAP_API_URL = "https://celltype.info/graphql"
CAP_AUTHENTICATE_USER_URL  = "authenticate-user-wg6qkl5yea-uc.a.run.app"
CAP_AUTHENTICATE_TOKEN_URL = "authenticate-token-wg6qkl5yea-uc.a.run.app"

class Cap(Client):
    def __init__(
            self,  
            login: str = None,
            pwd: str = None,
            custom_token: str = None  
        ) -> None:
        super().__init__(url = CAP_API_URL)
        self._login = login if login is not None else os.environ.get('CAP_LOGIN')
        self._pwd = pwd if pwd is not None else os.environ.get('CAP_PWD')
        self._custom_token = custom_token if custom_token is not None else os.environ.get('CAP_TOKEN')
        self._token: str = None
        self._token_expiry_time: time = None
        self._error_status: str = None

    def _request (
            self,
            url: str, 
            body: dict
        ) -> bool: 
        connection = http.client.HTTPSConnection(url)
        headers = {'Content-type': 'application/json'}
        connection.request("POST", url="",  body=json.dumps(body), headers=headers)
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
            if (self._request(CAP_AUTHENTICATE_TOKEN_URL, body)):
                return True
        if self._login is not None and self._pwd is not None:    
            body = {'email':self._login, 'password': self._pwd}
            if (self._request(CAP_AUTHENTICATE_USER_URL, body)):
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

    def download_urls(self, dataset_id: str) -> DownloadUrls:
        response = super().download_urls(dataset_id=dataset_id)
        return response
    
    def download_urls_json(self, dataset_id: str) -> str:
        response = self.download_urls(dataset_id)
        return response.model_dump_json()
    
    def file_status_json(self, dataset_id: str) -> str:
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

        response = self().embedding_clusters(
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
 
        response = self().embedding_data(
            self, 
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

