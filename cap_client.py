import asyncio
from graphql_client import Client
from graphql_client.custom_fields import (
    LabelFields,
    DatasetFields,
    DatasetDownloadUrlsResponseFields
)
from graphql_client.input_types import (
    DatasetSearchOptions,
    LookupDatasetsFiltersInput,
    LookupDatasetsSearchInput,
    SearchByMetadataArgs,
    CellLabelsSearchOptions,
    LookupLabelsFilters,
    LookupCellsSearch,
    SearchLabelByMetadataArgs
)
from graphql_client.custom_queries import Query
from graphql_client.custom_queries import Query

async def search_datasets(search=None, organism=None, tissue=None, assay=None, limit = 50, offset=0, sort=[]):
    # Create a client instance with the specified URL and headers
    client = Client(
        url="https://celltype.info/graphql" 
    )
    metadata = []
    if organism: 
        metadata.append(SearchByMetadataArgs(field="organism", values=organism))
    if tissue: 
        metadata.append(SearchByMetadataArgs(field="tissue", values=tissue))
    if assay: 
        metadata.append(SearchByMetadataArgs(field="assay", values=assay))

    search_options = DatasetSearchOptions(limit=limit, offset=offset, sort=sort)
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
        DatasetFields.project().id,
        DatasetFields.project().name,
        DatasetFields.labelsets().id,
        DatasetFields.labelsets().name,
        DatasetFields.labelsets().labels().id,
        DatasetFields.labelsets().labels().name,
        # DatasetFields.project().version,
        # DatasetFields.project().owner().display_name,
        # DatasetFields.labelsets().labels().count
    )

    # Execute the queries with an operation name
    response = await client.query(
        dataset_query,
        operation_name="SearchDatasets",
    )

    print(response)

async def search_cells(search=None, organism=None, tissue=None, assay=None, limit = 50, offset=0, sort=[]):
    # Create a client instance with the specified URL and headers
    client = Client(
        url="https://celltype.info/graphql" 
    )
    
    search_options = CellLabelsSearchOptions(limit=limit, offset=offset, sort=sort)

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
        LabelFields.labelset().id,
        LabelFields.labelset().name,
        LabelFields.labelset().labels().id, 
        LabelFields.labelset().labels().name,
        LabelFields.labelset().labels().count,
        LabelFields.labelset().dataset().id,
        LabelFields.labelset().dataset().name,
        LabelFields.labelset().dataset().project().id,
        LabelFields.labelset().dataset().project().name,
        # LabelFields.labelset().dataset().description,
        # LabelFields.labelset().dataset().project().version,
        # LabelFields.labelset().dataset().project().owner().display_name
    )  

    # Execute the queries with an operation name
    response = await client.query(
        lookup_query,
        operation_name="lookupCells",
    )

    print(response)

async def download_urls(id):
    # Create a client instance with the specified URL and headers
    client = Client(
        url="https://celltype.info/graphql" 
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

    print(response)

# Run the async function
asyncio.run(search_datasets(organism=["Homo sapiens"], tissue=[
  "stomach",
  "pyloric antrum",
  "body of stomach",
  "brain",
  "primary motor cortex",
  "prefrontal cortex",
  "parietal cortex",
  "primary visual cortex",
  "primary somatosensory cortex",
  "temporal cortex",
  "heart",
  "apex of heart",
  "heart right ventricle",
  "heart left ventricle",
  "interventricular septum",
  "sinoatrial node",
  "atrioventricular node",
  "right cardiac atrium",
  "left cardiac atrium"
]))
asyncio.run(download_urls(678))
asyncio.run(search_cells(organism=["Homo sapiens"], tissue=[
  "stomach",
  "pyloric antrum",
  "body of stomach",
  "brain",
  "primary motor cortex",
  "prefrontal cortex",
  "parietal cortex",
  "primary visual cortex",
  "primary somatosensory cortex",
  "temporal cortex",
  "heart",
  "apex of heart",
  "heart right ventricle",
  "heart left ventricle",
  "interventricular septum",
  "sinoatrial node",
  "atrioventricular node",
  "right cardiac atrium",
  "left cardiac atrium"
]))


