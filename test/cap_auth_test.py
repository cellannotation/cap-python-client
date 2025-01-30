import unittest
from unittest.mock import patch
from cap_client import Cap

class TestCap(unittest.TestCase):
    def setUp(self):
        self.cap = Cap()

    @patch.object(Cap, '_request')
    def test_authenticate_with_custom_token_success(self, mock_request):
        # Arrange
        mock_request.return_value = True
        self.cap._custom_token = "dummy_token"

        # Act
        result = self.cap._authenticate()

        # Assert
        self.assertTrue(result)
        mock_request.assert_called_once_with(
            "authenticate-token-wg6qkl5yea-uc.a.run.app",
            {'token': 'dummy_token'}
        )

    @patch.object(Cap, '_request')
    def test_authenticate_with_custom_token_failure(self, mock_request):
        # Arrange
        mock_request.return_value = False
        self.cap._custom_token = "dummy_token"

        # Act
        result = self.cap._authenticate()

        # Assert
        self.assertFalse(result)
        mock_request.assert_called_once()

    @patch.object(Cap, '_request')
    def test_authenticate_with_credentials_success(self, mock_request):
        # Arrange
        mock_request.return_value = True
        self.cap._custom_token = None
        self.cap._login = "test@example.com"
        self.cap._pwd = "password123"

        # Act
        result = self.cap._authenticate()

        # Assert
        self.assertTrue(result)
        mock_request.assert_called_once_with(
            "authenticate-user-wg6qkl5yea-uc.a.run.app",
            {'email': 'test@example.com', 'password': 'password123'}
        )

    @patch.object(Cap, '_request')
    def test_authenticate_with_credentials_failure(self, mock_request):
        # Arrange
        mock_request.return_value = False
        self.cap._custom_token = None
        self.cap._login = "test@example.com"
        self.cap._pwd = "password123"

        # Act
        result = self.cap._authenticate()

        # Assert
        self.assertFalse(result)
        mock_request.assert_called_once()

    def test_authenticate_with_no_credentials(self):
        # Arrange
        self.cap._custom_token = None
        self.cap._login = None
        self.cap._pwd = None

        # Act
        result = self.cap._authenticate()

        # Assert
        self.assertFalse(result)
        self.assertEqual(
            self.cap.error_status,
            "Missing CAP client authetication settings. Check CAP_LOGIN, CAP_PWD or CAP_TOKEN enviroment variables."
        )

if __name__ == '__main__':
    unittest.main()