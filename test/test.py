from cap_client import search_datasets, download_urls, search_cells 

def test_search_datasets():
    response = search_datasets(search="blood", organism=["Homo sapiens"], tissue=[
        "stomach",
        "pyloric antrum",
        "body of stomach"
        ], sort=[{"name":"ASC"}])
    print(response)

def test_download_urls():
    response = download_urls(678)
    print(response)

def test_search_cells():
    response = search_cells(search="blood", organism=["Homo sapiens"], tissue=[
        "parietal cortex",
        ], sort=[{"name":"ASC"}])
    print(response)

test_search_datasets()
test_download_urls()
test_search_cells()