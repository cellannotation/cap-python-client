# Generated by ariadne-codegen

from .base_client import BaseClient
from .base_model import BaseModel, Upload
from .client import Client
from .download_urls import DownloadUrls, DownloadUrlsDownloadUrls
from .exceptions import (
    GraphQLClientError,
    GraphQLClientGraphQLError,
    GraphQLClientGraphQLMultiError,
    GraphQLClientHttpError,
    GraphQLClientInvalidResponseError,
)
from .fragments import (
    CellLabelResult,
    CellLabelResultLabelset,
    CellLabelResultLabelsetDataset,
    CellLabelResultLabelsetDatasetLabelsets,
    CellLabelResultLabelsetDatasetLabelsetsLabels,
    CellLabelResultLabelsetDatasetProject,
    DatasetResult,
    DatasetResultLabelsets,
    DatasetResultLabelsetsLabels,
    DatasetResultProject,
    GeneLinkLabelset,
    GeneLinkLabelsetLabels,
    ProjectAuthorsProject,
    ProjectAuthorsProjectOwner,
    ProjectAuthorsProjectPermissions,
    ProjectAuthorsProjectPermissionsUser,
)
from .input_types import (
    CellLabelsSearchOptions,
    CellLabelsSearchSort,
    DatasetSearchOptions,
    DatasetSearchSort,
    LookupCellsSearch,
    LookupDatasetsFiltersInput,
    LookupDatasetsSearchInput,
    LookupLabelsFilters,
    SearchByMetadataArgs,
    SearchLabelByMetadataArgs,
)
from .lookup_cells import LookupCells, LookupCellsLookupCells
from .search_datasets import SearchDatasets, SearchDatasetsResults

from typing import List, Dict

def search_datasets(
    url: str = "https://celltype.info/graphql",
    search: List[str] = None,
    organism: List[str] = None,
    tissue: List[str] = None,
    assay: List[str] = None,
    limit: int = 50,
    offset: int = 0,
    sort: List[Dict[str, str]] = [],
):
    # Create a client instance with the specified URL and headers
    client = Client(url=url)

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

    response = client.search_datasets(
        options=search_options, filter=search_filter, search=search_input
    )
    return response

def search_cell_labels(
    url: str = "https://celltype.info/graphql",
    search: List[str] = None,
    organism: List[str] = None,
    tissue: List[str] = None,
    assay: List[str] = None,
    limit: int = 50,
    offset: int = 0,
    sort: List[Dict[str, str]] = [],
):
    # Create a client instance with the specified URL and headers
    client = Client(url=url)

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

    response = client.lookup_cells(
        options=search_options, filter=search_filter, search=search_input
    )
    return response

def download_urls(dataset_id: str, url: str = "https://celltype.info/graphql"):
    # Create a client instance with the specified URL and headers
    client = Client(url=url)

    # Execute the queries with an operation name
    response = client.download_urls(dataset_id=id)

    return response



__all__ = [
    "BaseClient",
    "BaseModel",
    "CellLabelResult",
    "CellLabelResultLabelset",
    "CellLabelResultLabelsetDataset",
    "CellLabelResultLabelsetDatasetLabelsets",
    "CellLabelResultLabelsetDatasetLabelsetsLabels",
    "CellLabelResultLabelsetDatasetProject",
    "CellLabelsSearchOptions",
    "CellLabelsSearchSort",
    "Client",
    "DatasetResult",
    "DatasetResultLabelsets",
    "DatasetResultLabelsetsLabels",
    "DatasetResultProject",
    "DatasetSearchOptions",
    "DatasetSearchSort",
    "DownloadUrls",
    "DownloadUrlsDownloadUrls",
    "GeneLinkLabelset",
    "GeneLinkLabelsetLabels",
    "GraphQLClientError",
    "GraphQLClientGraphQLError",
    "GraphQLClientGraphQLMultiError",
    "GraphQLClientHttpError",
    "GraphQLClientInvalidResponseError",
    "LookupCells",
    "LookupCellsLookupCells",
    "LookupCellsSearch",
    "LookupDatasetsFiltersInput",
    "LookupDatasetsSearchInput",
    "LookupLabelsFilters",
    "ProjectAuthorsProject",
    "ProjectAuthorsProjectOwner",
    "ProjectAuthorsProjectPermissions",
    "ProjectAuthorsProjectPermissionsUser",
    "SearchByMetadataArgs",
    "SearchDatasets",
    "SearchDatasetsResults",
    "SearchLabelByMetadataArgs",
    "Upload",
    "search_datasets",
    "search_cell_labels",
    "download_urls"
]
