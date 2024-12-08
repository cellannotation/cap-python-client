from typing import List, Any, Optional, Dict
from graphql_client import Client
from graphql_client.custom_fields import (
    LabelFields,
    LabelsetFields,
    DatasetFields,
    ProjectFields,
    CapUserFields,
    DatasetDownloadUrlsResponseFields
)
from graphql_client.input_types import (
    DatasetSearchOptions,
    LookupDatasetsFiltersInput,
    LookupDatasetsSearchInput,
    SearchByMetadataArgs,
    DatasetSearchSort,
    CellLabelsSearchOptions,
    LookupLabelsFilters,
    LookupCellsSearch,
    SearchLabelByMetadataArgs,
    CellLabelsSearchSort
)
from graphql_client.custom_queries import Query
from graphql_client.custom_queries import Query

async def search_datasets(url: str="https://celltype.info/graphql", search: List[str]=None, organism: List[str]=None, tissue: List[str]=None, assay: List[str]=None, limit: int=50, offset: int=0, sort: List[Dict[str,str]]=[]):
    # Create a client instance with the specified URL and headers
    client = Client(
        url=url 
    )

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

    search_filter = LookupDatasetsFiltersInput(metadata = metadata)
    search_input =  None
    if search:
        search_input =  LookupDatasetsSearchInput(name=search)

    # Build the queries
    dataset_query = Query.lookup_datasets(
        options=search_options, 
        filter=search_filter,
        search=search_input).fields(
        DatasetFields.id,
        DatasetFields.name,
        DatasetFields.description,
        DatasetFields.cell_count,
        DatasetFields.labelsets().fields(
            LabelsetFields.id,
            LabelsetFields.name,
            LabelsetFields.description,
            LabelsetFields.labels().fields(
                LabelFields.id,
                LabelFields.name,
                LabelFields.count,
            )
        ),
        DatasetFields.project().fields(
            ProjectFields.id,
            ProjectFields.name,
            ProjectFields.version,
            ProjectFields.description,
            ProjectFields.owner().fields(
                CapUserFields.display_name
            )
        )
    )

    # Execute the queries with an operation name
    response = await client.query(
        dataset_query,
        operation_name="SearchDatasets",
    )

    return response 

async def search_cells(url: str="https://celltype.info/graphql", search: List[str]=None, organism: List[str]=None, tissue: List[str]=None, assay: List[str]=None, limit: int=50, offset: int=0, sort: List[Dict[str,str]]=[]):
    # Create a client instance with the specified URL and headers
    client = Client(
        url=url 
    )
    
    sorting = []
    for item in sort:
        key = list(item.keys())[0]
        value = list(item.values())[0]
        sorting.append(CellLabelsSearchSort(field=key, order=value))
    search_options = CellLabelsSearchOptions(limit=limit, offset=offset, sort=sorting)

    metadata = []
    if organism: 
        metadata.append(SearchLabelByMetadataArgs(field="organism", values=organism))
    if tissue: 
        metadata.append(SearchLabelByMetadataArgs(field="tissue", values=tissue))
    if assay: 
        metadata.append(SearchLabelByMetadataArgs(field="assay", values=assay))
  
    search_filter = LookupLabelsFilters(metadata = metadata)

    search_input = None
    if search:
        search_input =  LookupCellsSearch(name=search)

    # Build the queries
    lookup_query = Query.lookup_cells(options=search_options, filter=search_filter, search=search_input).fields(
        LabelFields.id,
        LabelFields.full_name,
        LabelFields.name,
        LabelFields.ontology_term_exists,
        LabelFields.ontology_term_id,
        LabelFields.ontology_term,
        LabelFields.synonyms,
        LabelFields.category_ontology_term_exists,
        LabelFields.category_ontology_term_id,
        LabelFields.category_ontology_term,
        LabelFields.category_full_name,
        LabelFields.marker_genes,
        LabelFields.canonical_marker_genes,
        LabelFields.count,
        LabelFields.ontology_assessment,
        LabelFields.labelset().fields(
            LabelsetFields.id,
            LabelsetFields.name,
            LabelsetFields.description,
            LabelsetFields.dataset().fields(
                DatasetFields.id,
                DatasetFields.name,
                DatasetFields.project().fields(
                    ProjectFields.id,
                    ProjectFields.name,
                    ProjectFields.version,
                )
            )
        )
    )  

    # Execute the queries with an operation name
    response = await client.query(
        lookup_query,
        operation_name="lookupCells",
    )

    return response 

async def download_urls(id: int, url: str="https://celltype.info/graphql"):
    # Create a client instance with the specified URL and headers
    client = Client(
        url=url 
    )

    # Build the queries
    download_query = Query.download_urls(dataset_id=id).fields(
        DatasetDownloadUrlsResponseFields.ann_data_url,
        DatasetDownloadUrlsResponseFields.seurat_url,
        DatasetDownloadUrlsResponseFields.cap_json_url_tar,
        DatasetDownloadUrlsResponseFields.cap_json_url_zip
    )  

    # Execute the queries with an operation name
    response = await client.query(
        download_query,
        operation_name="DownloadUrls",
    )

    return response

import asyncio
def test_search_datasets():
    response = asyncio.run(search_datasets(search="blood", organism=["Homo sapiens"], tissue=[
        "stomach",
        "pyloric antrum",
        "body of stomach"
        ], sort=[{"name":"ASC"}]))
    print(response)

def test_download_urls():
    response = asyncio.run(download_urls(678))
    print(response)

def test_search_cells():
    response = asyncio.run(search_cells(search="blood", organism=["Homo sapiens"], tissue=[
        "parietal cortex",
        ], sort=[{"name":"ASC"}]))
    print(response)

test_search_datasets()
test_download_urls()
test_search_cells()