from typing import List, Dict
import time
import http.client
import json
import jwt

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
)
from .client.download_urls import DownloadUrls
from .client.lookup_cells import LookupCells
from .client.search_datasets import SearchDatasets

CAP_API_URL = "https://celltype.info/graphql"
CAP_AUTHORIZE_URL = "authenticate-user-wg6qkl5yea-uc.a.run.app"
class Cap(Client):
    def __init__(self, login = None, pwd = None, authorize_url = CAP_AUTHORIZE_URL) -> None:
        super().__init__(url = CAP_API_URL),
        self._authorize_url = authorize_url,
        self._login: str = login,
        self._pwd: str = pwd,
        self._token: str = None,
        self._token_expiry_time: time = None,
        self._error_status: str = None,

    def _authenticate(
        self  
     ) -> bool:
        if self._login is None or self._pwd is None:
            self._token = None
            self._token_expiry_time = None
            self._error_status = "No credentials"
            return False
        if (self._token is None or self._token_expiry_time is None or time.time() >= self._token_expiry_time ):
            self._token = None
            self._token_expiry_time = None            
            connection = http.client.HTTPSConnection(self._authorize_url)
            headers = {'Content-type': 'application/json'}
            body = {'email':self._login, 'password': self._pwd}
            connection.request("POST", url="",  body=json.dumps(body), headers=headers)
            response = connection.getresponse()
            if (response.status == 200):
                try:
                    response = response.read().decode()
                    self._token = json.loads(response)['idToken']
                    self._token_expiry_time = jwt.decode(self._token, options={"verify_signature": False})['exp']
                    self._error_status = None
                    return True
                except: 
                    self._error_status = "Failed to parse 200 OK response to get ID token"
                    return False                
            self._error_status = "Failed to get ID token " + response.status + response.reason
            return False
        else:
            return True

    def search_datasets(
        self,
        search: List[str] = None,
        organism: List[str] = None,
        tissue: List[str] = None,
        assay: List[str] = None,
        limit: int = 50,
        offset: int = 0,
        sort: List[Dict[str, str]] = [],
    ) -> str:
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
    ) -> str:
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
        return response.model_dump_json()

    def download_urls(self, dataset_id: str) -> str:

        response = super().download_urls(dataset_id=dataset_id)
        return response.model_dump_json()
