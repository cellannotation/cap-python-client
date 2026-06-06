from typing import Any, Dict, Mapping, Tuple


PERSISTED_QUERY_IDS: Mapping[str, str] = {
    "CreateDatasetSession": "3d4c659070185075aca36641f8adebdc1a5abdf0ba52396990624e8b980df235",
    "DatasetDataQuery": "0bf580de5e51d602a103067cf8cab04d4f7f7ece914e95e02ee17a2b5b6e403a",
    "DatasetReadiness": "97f3fe6ae4e98f449eca68a663b445abd1dd245b9346dd65ac5811c92e60c6df",
    "DownloadUrls": "2f3dba0f60c5bc24355329a34f78a3adcea5ce3967d4b69613b7a0b83707286b",
    "EmbeddingData": "61dd5234267ce1ac69dd0eaa9691315614ede21aa684326fe2ed5c5df01b211c",
    "FilesStatus": "52379360efe8f4e5817b4ffd0b72fe0cceafa83293eae8cac7fe121b0e706ecb",
    "GeneralDE": "d16f2c801e1cb4f81905b4dbd400887518789be1e3875b93123511658525bd8a",
    "Heatmap": "f7996dd71e84df72e05d0fcc504cc1eb261102bed7b02568680687da8748eef7",
    "HighlyVariableGenes": "f23dfa3723a3720e469bc036f86f9501962c9c838477ed8d0c7e02a1aeae428c",
    "LookupCells": "8799894aedfb3533dcdf37615b8dd04d4d9308d59a72d62a0a9856274633c239",
    "MDCommonsQuery": "584e91f0ee408d633394d3d350d1deeb6439a514928983a7b8621837a4e056f1",
    "SearchDatasets": "5953956a6e6e0f5fe5b7aa2f1154fe672523ce5535bb1241fa93c2b8fce7b8f0",
}

OPERATION_NAME_OVERRIDES: Mapping[str, str] = {
    "CreateSession": "CreateDatasetSession",
    "DatasetInitialStateQuery": "DatasetDataQuery",
    "DatasetReady": "DatasetReadiness",
    "MDReady": "DatasetReadiness",
}

VARIABLES_TO_DROP: Mapping[str, Tuple[str, ...]] = {
    "DatasetInitialStateQuery": ("labelsetOrder",),
}


def persisted_operation_name(operation_name: str) -> str:
    return OPERATION_NAME_OVERRIDES.get(operation_name, operation_name)


def persisted_query_id(operation_name: str) -> str:
    return PERSISTED_QUERY_IDS[persisted_operation_name(operation_name)]


def persisted_variables(
    operation_name: str, variables: Dict[str, Any]
) -> Dict[str, Any]:
    names_to_drop = VARIABLES_TO_DROP.get(operation_name)
    if not names_to_drop:
        return variables

    return {key: value for key, value in variables.items() if key not in names_to_drop}
