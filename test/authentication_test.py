from cap_client import Cap 
import os
import time

def test_authentication_by_right_credentials_user():
    cap = Cap()
    login = os.environ.get('CAP_LOGIN')
    pwd = os.environ.get('CAP_PWD')
    if login is None or pwd is None:
        assert "Either CAP_LOGIN or CAP_PWD or both env variables are empty."
    else:
        # considering right credentials
        assert cap._authenticate() is True
        assert cap.get_id_token() is not None
        assert cap.get_token_expiry_time() > time.time()
        assert cap.get_error_status() is None

def test_authentication_by_right_token():
    cap = Cap()
    token = os.environ.get('CAP_TOKEN')
    if token is None:
        assert "CAP_TOKEN env variable is empty."
    else:
        # considering correct token
        assert cap._authenticate() is True
        assert cap.get_id_token() is not None
        assert cap.get_token_expiry_time() > time.time()
        assert cap.get_error_status() is None

def test_authentication_by_wrong_credentials_user():
    cap = Cap(login = 'Not existing user', pwd = 'Password')
    assert cap._authenticate() is False
    assert cap.get_id_token() is None
    assert cap.get_token_expiry_time() is None
    assert cap.get_error_status() is not None

def test_authentication_by_wrong_token():
    cap = Cap(login = '', pwd = '', custom_token = 'Not existing token')
    assert cap._authenticate() is False
    assert cap.get_id_token() is None
    assert cap.get_token_expiry_time() is None
    assert cap.get_error_status() is not None

def test_empty_credentials():
    cap = Cap(login = '', pwd = '', custom_token = '')
    assert cap._authenticate() is False
    assert cap.get_id_token() is None
    assert cap.get_error_status() is not None
