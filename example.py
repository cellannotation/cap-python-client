import json
from cap_client import Cap

cap = Cap(
    url = "https://celltype.info/graphql", 
    auth_url = "us-central1-capv2-gke-prod.cloudfunctions.net",
    login = "<login>",
    pwd = "<password>" 
)

# public API 

datasets = cap.search_datasets()

# for dataset in datasets.results:
dataset  = datasets.results[1]
print("Processing dataset id: ", dataset.id) 

print("Files status")
cap.files_status(dataset.id)

print("Dataset initial query")
snapshot = cap.dataset_initial_state_query(dataset.id)

print("Create session")
session_id = "123qwerty"
# TODO snapshot should be compatible for session creation 
# OR should be the endpoint to get a snapshot for session creation
embeddings = cap.create_session(session_id, snapshot.model_dump())

print("General DE")
labelset = dataset.labelsets[1]    
cap.general_de(dataset_id = dataset.id, labelset_id = labelset.id, session_id = session_id)

# TODO: Cover full MD page cycle '''

# authorized API 

'''
if cap._authenticate() == True:
    # authorized API call

'''    