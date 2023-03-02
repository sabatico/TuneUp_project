import os as os
import sys as sys

import pytest

from factory.app_factory import create_app
from flask import Flask


import socket as socket


pytest.fixture(scope="function",autouse=True)
def setup_class():
    pass


def teardown_class():
    pass

def test_app_is_instance_of_flask():
    app = create_app()
    with app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405

