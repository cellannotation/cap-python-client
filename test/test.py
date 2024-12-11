from cap_client import Cap 

cap = Cap()

def test_search_datasets():
    response = cap.search_datasets(search="blood", organism=["Homo sapiens"], tissue=[
        "stomach",
        "pyloric antrum",
        "body of stomach"
        ], sort=[{"name":"ASC"}])
    print(response)

def test_download_urls():
    response = cap.download_urls(678)
    print(response)

def test_search_cells():
    response = cap.search_cell_labels(search="blood", organism=["Homo sapiens"], tissue=[
        "parietal cortex",
        ], sort=[{"name":"ASC"}])
    print(response)

test_search_datasets()
test_download_urls()
test_search_cells()