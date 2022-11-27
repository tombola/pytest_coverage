import pytest
import requests


# Skip mark is provided by pytest
@pytest.mark.skip
def test_api_call():
    """
    If run this should fail because requests.get is monkeypatched, see conftest.py
    """
    requests.get("https://google.com")
