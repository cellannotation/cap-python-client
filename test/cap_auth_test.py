import pytest
from unittest.mock import patch, Mock
from cap_client import Cap

CAP_AUTHENTICATE_URL = "us-central1-capv2-gke-prod.cloudfunctions.net" 

def test_authenticate_with_custom_token_success():
    cap = Cap()
    with patch.object(Cap, '_request') as mock_request:
        mock_request.return_value = True
        cap._custom_token = "dummy_token"

        result = cap._authenticate()

        assert result is True
        mock_request.assert_called_once_with(
            base_url='us-central1-capv2-gke-prod.cloudfunctions.net', 
            url='/authenticate-token', 
            body={'token': 'dummy_token'}
        )

def test_authenticate_with_custom_token_failure():
    cap = Cap()
    with patch.object(Cap, '_request') as mock_request:
        mock_request.return_value = False
        cap._custom_token = "dummy_token"

        result = cap._authenticate()

        assert result is False
        mock_request.assert_called_once()

def test_authenticate_with_credentials_success():
    cap = Cap()
    with patch.object(Cap, '_request') as mock_request:
        # Arrange
        mock_request.return_value = True
        cap._custom_token = None
        cap._login = "test@example.com"
        cap._pwd = "password123"

        # Act
        result = cap._authenticate()

        # Assert
        assert result is True
        mock_request.assert_called_once_with(
           base_url='us-central1-capv2-gke-prod.cloudfunctions.net', 
           url='/authenticate-user', 
           body={'email': 'test@example.com', 'password': 'password123'}
        )

def test_authenticate_with_credentials_failure():
    cap = Cap()
    with patch.object(Cap, '_request') as mock_request:
        # Arrange
        mock_request.return_value = False
        cap._custom_token = None
        cap._login = "test@example.com"
        cap._pwd = "password123"

        # Act
        result = cap._authenticate()

        # Assert
        assert result is False
        mock_request.assert_called_once()

def test_authenticate_with_no_credentials():
    cap = Cap()
    # Arrange
    cap._custom_token = None
    cap._login = None
    cap._pwd = None

    # Act
    result = cap._authenticate()

    # Assert
    assert result is False
    assert cap.error_status == "Missing CAP client authetication settings. Check CAP_LOGIN, CAP_PWD or CAP_TOKEN enviroment variables."
        