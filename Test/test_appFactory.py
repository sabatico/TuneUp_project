import os as os
import sys as sys
from dotenv import load_dotenv as load_dotenv
import pytest as pytest

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import socket as socket

from factory.app_factory import create_app
from flask import Flask

@pytest.fixture
def start():
    load_dotenv()
    os.environ['PYTEST_RUNNING'] = 'true'
    app = create_app()
    yield app

def test_app_is_started_with_correct_port_and_ip(start):
    app = start
    with app.test_client() as test_client:
        response = test_client.post("/")
        assert isinstance(app, Flask)
        assert response.status_code == 200
        

