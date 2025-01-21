from cap_client import Cap 
import json

cap = Cap()

def test_search_datasets():
    response = cap.search_datasets(search="blood", organism=["Homo sapiens"], tissue=[
        "stomach",
        "pyloric antrum",
        "body of stomach"
        ], sort=[{"name":"ASC"}])
    json_result = json.loads(response)
    assert json_result["results"] is not None


def test_download_urls():
    response = cap.download_urls(678)
    json_result = json.loads(response)
    assert json_result["download_urls"] is not None

def test_search_cells():
    response = cap.search_cell_labels(search="blood", organism=["Homo sapiens"], tissue=[
        "parietal cortex",
        ], sort=[{"name":"ASC"}])
    json_result = json.loads(response)
    assert json_result["lookup_cells"] is not None