from flask import Flask

from factory.data_factory import DataFactory
from routes import pages

import pytest as pytest
from pytest_mock import mocker



@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    return app


def test_index_returns_template(app):
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"<!DOCTYPE html>" in response.data
        assert b"Collect Data" in response.data



def test_index_starts_thread(app, mocker):
    mocker.patch('factory.data_factory.DataFactory.collect_data_framework')
    with app.test_client() as client:
        client.get("/?collect=start")
        factory_instance = DataFactory
        factory_instance.collect_data_framework.assert_called_once()
    

def test_get_data_collection_progress(app,monkeypatch):
    mock_data= [["cpu", 25.0], ["memory", 50.0], ["disk", 75.0], ["network", 100.0]]
    monkeypatch.setattr('routes.index.data_collection',mock_data)
    
    with app.test_client() as client:
        
        response = client.get("/get_data_collection_progress")
        assert response.status_code == 200