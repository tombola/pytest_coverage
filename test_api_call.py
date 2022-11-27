import requests

def test_api_call():
    """
    This should fail because requests.get is monkeypatched, see conftest.py
    """
    requests.get("https://google.com")
