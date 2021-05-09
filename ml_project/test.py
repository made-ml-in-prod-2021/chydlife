import pytest
import pandas as pd
import warnings
from homework1 import pipeline
from data.read_and_process import read_process_data, split_train_val_data
data_test_path = "ml_project/data_for_tes/example.csv"


def test_read_and_process():
    heart_data_example = read_process_data(data_test_path)
    assert len(heart_data_example) == 303

def test_split_data():
    heart_data_example = read_process_data(data_test_path)
    x_train, x_test, y_train, y_test = split_train_val_data(heart_data_example)
    assert round(len(x_train) / (len(x_test) + len(x_train)), 1) == 0.8

def test_pipeline():
    score_train, score_test = pipeline('ml_project/data', 'ml_project/config/config.yml','ml_project/results')
    assert score_train > score_test 