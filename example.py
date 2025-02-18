import json
from cap_client import Cap
from cap_client.client.input_types import DatasetObjectInput

cap = Cap(
    url = "https://rc1.celltype.info/graphql", 
    auth_url = "us-central1-capv2-gke-rc1.cloudfunctions.net",
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
# TODO DatasetIntialStateQuery should be compatible with DatasetObjectInput 
# OR should be the endpoint to get a snapshot for session creation
snapshot = snapshot.model_dump()
embeddings = cap.create_session(session_id = session_id, dataset = DatasetObjectInput(**snapshot))

print("General DE")
labelset = dataset.labelsets[1]    
cap.general_de(dataset_id = dataset.id, labelset_id = labelset.id, session_id = session_id)

# TODO: Cover full MD page cycle '''

# authorized API 

'''
if cap._authenticate() == True:
    # authorized API call

'''    