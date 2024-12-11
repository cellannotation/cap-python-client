from typing import List, Dict

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


class Cap(Client):
    def __init__(self) -> None:
        super().__init__(url="https://celltype.info/graphql")

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
