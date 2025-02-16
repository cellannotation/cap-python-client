import pytest
import json
from unittest.mock import patch, Mock
from cap_client import Cap

CAP_AUTHENTICATE_USER_URL  = "authenticate-user-wg6qkl5yea-uc.a.run.app"
CAP_AUTHENTICATE_TOKEN_URL = "authenticate-token-wg6qkl5yea-uc.a.run.app"

def test_search_datasets():
    # Arrange
    cap = Cap()
    sample_dataset_response = '{"results": [{"id": "123", "name": "Test Dataset"}]}'
    with patch.object(Cap, 'search_datasets_json') as search_request_mock:
        search_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.search_datasets_json(
            search=["blood"],
            organism=["Homo sapiens"],
            tissue=["stomach"],
            assay=["10x 3' v1"],
            sort=[{"name":"ASC"}],
            limit=10,
            offset=0
        )

        # Assert
        assert result == '{"results": [{"id": "123", "name": "Test Dataset"}]}'
        search_request_mock.assert_called_once()

def test_search_datasets_no_params():
    # Arrange
    cap = Cap()
    sample_dataset_response = '{"results": [{"id": "123", "name": "Test Dataset"}]}'
    with patch.object(Cap, 'search_datasets_json') as search_request_mock:
        search_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.search_datasets_json()

        # Assert
        assert result == '{"results": [{"id": "123", "name": "Test Dataset"}]}'
        search_request_mock.assert_called_once()

def test_download_urls():
    # Arrange
    cap = Cap()
    sample_url_response = '{"download_urls": [{"annDataUrl": "gs://test_bucket/dataset.h5ad"}]}'
    with patch.object(Cap, 'download_urls_json') as download_request_mock:
        download_request_mock.return_value = sample_url_response

        # Act
        result = cap.download_urls_json(1)

        # Assert
        assert result == '{"download_urls": [{"annDataUrl": "gs://test_bucket/dataset.h5ad"}]}'
        download_request_mock.assert_called_once()

def test_download_urls_no_params():
    # Arrange
    cap = Cap()
    sample_url_response = '{"errors": [{"message": "Failed to get download urls"}]}'
    with patch.object(Cap, 'download_urls_json') as download_request_mock:
        download_request_mock.return_value = sample_url_response

        # Act
        result = cap.download_urls_json()

        # Assert
        assert result == '{"errors": [{"message": "Failed to get download urls"}]}'
        download_request_mock.assert_called_once()

def test_search_cells():
    cap = Cap()
    sample_cell_labels_response = '{"lookup_cells": [{"id": "123", "name": "Test Cell Label"}]}'
    with patch.object(Cap, 'search_cell_labels_json') as search_request_mock:
        search_request_mock.return_value = sample_cell_labels_response

        # Act
        result = cap.search_cell_labels_json(
            search="blood", 
            organism=["Homo sapiens"], 
            tissue=["parietal cortex"],
            assay=["10x 3' v1"], 
            sort=[{"name":"ASC"}],
            limit=10,
            offset=0
        )

        # Assert
        assert result == '{"lookup_cells": [{"id": "123", "name": "Test Cell Label"}]}'
        search_request_mock.assert_called_once()
 
def test_search_cells_no_params():
    cap = Cap()
    sample_dataset_response = '{"lookup_cells": [{"id": "123", "name": "Test Cell Label"}]}'
    with patch.object(Cap, 'search_cell_labels_json') as search_request_mock:
        search_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.search_cell_labels_json()

        # Assert
        assert result == '{"lookup_cells": [{"id": "123", "name": "Test Cell Label"}]}'
        search_request_mock.assert_called_once()

def test_files_status_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "getMdFilesStatus": "ready" } } }'
    with patch.object(Cap, 'files_status_json') as files_status_request_mock:
        files_status_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.files_status_json("1")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "getMdFilesStatus": "ready" } } }'
        files_status_request_mock.assert_called_once()

def test_files_status_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.files_status_json()
        assert False
    except TypeError as e:
       assert True

def test_md_commons_query_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "embeddings": [] } } }'
    with patch.object(Cap, 'md_commons_query_json') as md_commons_query_request_mock:
        md_commons_query_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.md_commons_query_json("1")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "embeddings": [] } } }'
        md_commons_query_request_mock.assert_called_once()

def test_md_commons_query_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.md_commons_query_json()
        assert False
    except TypeError as e:
       assert True
    
def test_dataset_initial_state_query_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "name": "dataset"} } }'
    with patch.object(Cap, 'dataset_initial_state_query_json') as dataset_initial_state_query_request_mock:
        dataset_initial_state_query_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.dataset_initial_state_query_json("1")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "name": "dataset"} } }'
        dataset_initial_state_query_request_mock.assert_called_once()

def test_dataset_initial_state_query_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.dataset_initial_state_query_json()
        assert False
    except TypeError as e:
       assert True
    
def test_cluster_types_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "embeddingClusterTypes": [] } } }'
    with patch.object(Cap, 'cluster_types_json') as cluster_types_request_mock:
        cluster_types_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.cluster_types_json("1")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "embeddingClusterTypes": [] } } }'
        cluster_types_request_mock.assert_called_once()

def test_cluster_types_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.cluster_types_json()
        assert False
    except TypeError as e:
       assert True

def test_embeddings_clusters_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "embeddingCluster": [] } } }'
    with patch.object(Cap, 'embeddings_clusters_json') as embeddings_clusters_request_mock:
        embeddings_clusters_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.embeddings_clusters_json(dataset_id = "1", cluster = "cluster")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "embeddingCluster": [] } } }'
        embeddings_clusters_request_mock.assert_called_once()

def test_embeddings_clusters_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.embeddings_clusters_json()
        assert False
    except TypeError as e:
       assert True

def test_embedding_data_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "embeddingData": {} } } } }'
    with patch.object(Cap, 'embedding_data_json') as embedding_data_request_mock:
        embedding_data_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.embedding_data_json(dataset_id = "1", embedding = "embedding", scale_max_plan = 1000, session_id = "123")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "embeddingData": {} } } } }'
        embedding_data_request_mock.assert_called_once()

def test_embedding_data_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.embedding_data_json()
        assert False
    except TypeError as e:
       assert True

def test_general_de_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "generalDiff": "" } } } }'
    with patch.object(Cap, 'general_de_json') as general_de_request_mock:
        general_de_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.general_de_json(dataset_id = "1", labelset_id = "1", random_seed = 1, session_id = "123")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "generalDiff": "" } } } }'
        general_de_request_mock.assert_called_once()

def test_general_de_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.general_de_json()
        assert False
    except TypeError as e:
       assert True

def test_heatmap_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "embeddingDiffHeatMap": {} } } } }'
    with patch.object(Cap, 'heatmap_json') as heatmap_request_mock:
        heatmap_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.heatmap_json(dataset_id = "1", diff_key = "kgjgjgk")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "embeddingDiffHeatMap": {} } } } }'
        heatmap_request_mock.assert_called_once()

def test_heatmap_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.heatmap_json()
        assert False
    except TypeError as e:
       assert True

def test_highly_variable_genes_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123", "embeddingHighlyVariableGenes": [] } } } }'
    with patch.object(Cap, 'highly_variable_genes_json') as highly_variable_genes_request_mock:
        highly_variable_genes_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.highly_variable_genes_json(dataset_id = "1", offset = 1, limit = 10)

        # Assert
        assert result == '{"data": { "dataset": { "id": "123", "embeddingHighlyVariableGenes": [] } } } }'
        highly_variable_genes_request_mock.assert_called_once()

def test_highly_variable_genes_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.highly_variable_genes_json()
        assert False
    except TypeError as e:
       assert True

def test_dataset_ready_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123" } } }'
    with patch.object(Cap, 'dataset_ready_json') as dataset_ready_request_mock:
        dataset_ready_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.dataset_ready_json("1")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123" } } }'
        dataset_ready_request_mock.assert_called_once()

def test_dataset_ready_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.dataset_ready_json()
        assert False
    except TypeError as e:
       assert True

def test_md_ready_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "dataset": { "id": "123" } } }'
    with patch.object(Cap, 'md_ready_json') as md_ready_request_mock:
        md_ready_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.md_ready_json("1")

        # Assert
        assert result == '{"data": { "dataset": { "id": "123" } } }'
        md_ready_request_mock.assert_called_once()

def test_md_ready_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.md_ready_json()
        assert False
    except TypeError as e:
       assert True

def test_create_session_json():
    cap = Cap()
    sample_dataset_response = '{"data": { "saveEmbeddingSession": { "id": "123", "name": "test" } } }'
    with patch.object(Cap, 'create_session_json') as create_session_request_mock:
        create_session_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.create_session_json(session_id = "1", data = {})

        # Assert
        assert result == '{"data": { "saveEmbeddingSession": { "id": "123", "name": "test" } } }'
        create_session_request_mock.assert_called_once()

def test_create_session_json_no_params():
    cap = Cap()
    try:
        # Act and Assert
        cap.create_session_json()
        assert False
    except TypeError as e:
       assert True