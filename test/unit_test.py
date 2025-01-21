import sys
import pytest


if __name__ == "__main__":
    files = [
        "public_api_test.py",
        "authentication_test.py"
    ]
    sys.exit(pytest.main(files))