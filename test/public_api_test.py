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
    with patch.object(Cap, 'search_datasets') as search_request_mock:
        search_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.search_datasets(
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
    with patch.object(Cap, 'search_datasets') as search_request_mock:
        search_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.search_datasets()

        # Assert
        assert result == '{"results": [{"id": "123", "name": "Test Dataset"}]}'
        search_request_mock.assert_called_once()

def test_download_urls():
    # Arrange
    cap = Cap()
    sample_url_response = '{"download_urls": [{"annDataUrl": "gs://test_bucket/dataset.h5ad"}]}'
    with patch.object(Cap, 'download_urls') as download_request_mock:
        download_request_mock.return_value = sample_url_response

        # Act
        result = cap.download_urls(1)

        # Assert
        assert result == '{"download_urls": [{"annDataUrl": "gs://test_bucket/dataset.h5ad"}]}'
        download_request_mock.assert_called_once()

def test_download_urls_no_params():
    # Arrange
    cap = Cap()
    sample_url_response = '{"errors": [{"message": "Failed to get download urls"}]}'
    with patch.object(Cap, 'download_urls') as download_request_mock:
        download_request_mock.return_value = sample_url_response

        # Act
        result = cap.download_urls()

        # Assert
        assert result == '{"errors": [{"message": "Failed to get download urls"}]}'
        download_request_mock.assert_called_once()

def test_search_cells():
    cap = Cap()
    sample_cell_labels_response = '{"lookup_cells": [{"id": "123", "name": "Test Cell Label"}]}'
    with patch.object(Cap, 'search_cell_labels') as search_request_mock:
        search_request_mock.return_value = sample_cell_labels_response

        # Act
        result = cap.search_cell_labels(
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
    with patch.object(Cap, 'search_cell_labels') as search_request_mock:
        search_request_mock.return_value = sample_dataset_response

        # Act
        result = cap.search_cell_labels()

        # Assert
        assert result == '{"lookup_cells": [{"id": "123", "name": "Test Cell Label"}]}'
        search_request_mock.assert_called_once()