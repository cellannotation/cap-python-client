import json
from cap_client import Cap

cap = Cap(
    url = "https://rc1.celltype.info/graphql", 
    auth_url = "us-central1-capv2-gke-rc1.cloudfunctions.net",
    login = "<login>",
    pwd = "<password>" 
)

# public API 

datasets = cap.search_datasets()

for dataset in datasets.results:
    print("Processing dataset id: ", dataset.id) 

    print("Files status")
    cap.files_status_json(dataset_id)

    print("Dataset initial query")
    cap.dataset_initial_state_query_json(dataset_id)

    # TODO: Cover full MD page cycle '''

# authorized API 

'''
if cap._authenticate() == True:
    # authorized API call

'''    