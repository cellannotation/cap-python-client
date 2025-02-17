import json
from cap_client import Cap

cap = Cap(
    url = "https://rc1.celltype.info/graphql", 
    auth_url = "us-central1-capv2-gke-rc1.cloudfunctions.net",
    login = "<login>",
    pwd = "<password>" 
)

# public API 

'''
datasets = json.loads(cap.search_datasets_json())
for dataset in datasets["results"]:
    dataset_id = dataset["id"]
    print("Processing dataset id: ", dataset_id) 

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