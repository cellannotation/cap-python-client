import asyncio
from graphql_client import Client
from graphql_client.custom_fields import (
    DatasetFields,
    DatasetDownloadUrlsResponseFields
)
from graphql_client.custom_queries import Query
from graphql_client.custom_queries import Query

async def search_datasets():
    # Create a client instance with the specified URL and headers
    client = Client(
        url="https://celltype.info/graphql" 
    )

    # Build the queries
    dataset_query = Query.lookup_datasets().fields(DatasetFields.id)

    # Execute the queries with an operation name
    response = await client.query(
        dataset_query,
        operation_name="SearchDatasets",
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
        DatasetDownloadUrlsResponseFields.seurat_url
    )  

    # Execute the queries with an operation name
    response = await client.query(
        download_query,
        operation_name="DownloadUrls",
    )

    print(response)

# Run the async function
asyncio.run(search_datasets())
asyncio.run(download_urls(678))

