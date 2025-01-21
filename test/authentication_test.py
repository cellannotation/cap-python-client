from cap_client import Cap 
import os

cap = Cap()

def test_empty_credentials():
    assert cap._authenticate() is False
    assert cap.get_error_status() == "Missing CAP client authetication settings. Check CAP_LOGIN, CAP_PWD or CAP_TOKEN enviroment variables."

def test_authentication_by_user():
    login = os.environ.get('CAP_LOGIN')
    pwd = os.environ.get('CAP_PWD')
    if login is None or pwd is None:
        assert cap._authenticate() is False
    else:
        # considering right credentials
        assert cap._authenticate() is True

def test_authentication_by_token():
    token = os.environ.get('CAP_TOKEN')
    if token is None:
        assert cap._authenticate() is False
    else:
        # considering correct token
        assert cap._authenticate() is True