"""
Pytest looks for a conftest.py module in each directory. 
can use fixtures from here  throughout the module’s parent directory 
and in any subdirectories without having to import it.

https://realpython.com/pytest-python-testing/#how-to-use-fixtures-at-scale
"""

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    """
    autouse parameter means this will take effect on all tests (see docstring)
    """
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
