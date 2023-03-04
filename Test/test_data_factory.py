import pytest
from factory.data_factory import DataFactory


def test_collect_data():
    """test if collected data returns summary and progress"""
    mock_data = {"cpu": 0.1, "memory": 0.2, "disk": 0.3, "network": 0.4}
    
    
    data = DataFactory()
    progress = data.collect_data_framework()
    
    assert progress[0][0] == "cpu" 
    assert progress[0][1] == 25.0
    assert progress[3][0] == "network" 
    assert progress[3][1] == 100.0
    assert len(progress) == len(mock_data)
    