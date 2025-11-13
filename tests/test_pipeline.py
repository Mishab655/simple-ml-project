import os
import pytest
import pandas as pd

def test_data_generation():
    assert os.path.exists('data/data.csv')

def test_model_training():
    assert os.path.exists('models/model.pkl')

def test_model_metrics():
    assert os.path.exists('models/metrics.json')
