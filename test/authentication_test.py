from cap_client import Cap 
import os
import time

cap = Cap()

def test_authentication_by_right_credentials_user():
    login = os.environ.get('CAP_LOGIN')
    pwd = os.environ.get('CAP_PWD')
    if login is None or pwd is None:
        assert False, "Either CAP_LOGIN or CAP_PWD or both env variables are empty."
    else:
        # considering right credentials
        assert cap._authenticate() is True
        assert cap.get_id_token() is not None
        assert cap.get_token_expiry_time() > time.time()
        assert cap.get_error_status() is None

def test_authentication_by_right_token():
    token = os.environ.get('CAP_TOKEN')
    if token is None:
        assert False, "CAP_TOKEN env variable is empty."
    else:
        # considering correct token
        assert cap._authenticate() is True
        assert cap.get_id_token() is not None
        assert cap.get_token_expiry_time() > time.time()
        assert cap.get_error_status() is None

