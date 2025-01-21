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
)

CAP_API_URL = "https://celltype.info/graphql"
CAP_AUTHENTICATE_USER_URL = "authenticate-user-wg6qkl5yea-uc.a.run.app"
CAP_AUTHENTICATE_TOKEN_URL = "authenticate-token-wg6qkl5yea-uc.a.run.app"
class Cap(Client):
    def __init__(self) -> None:
        super().__init__(url = CAP_API_URL)
        self._login: str = os.environ.get('CAP_LOGIN')
        self._pwd: str = os.environ.get('CAP_PWD')
        self._custom_token: str = os.environ.get('CAP_TOKEN')
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
           
    def get_error_status(
            self
    ) -> str:
        return self._error_status
    
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
