import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import logging
import sys
import yaml
import click
import warnings
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from data.read_and_process import read_process_data, split_train_val_data
from model.models_and_prediction import validation, build_model, prediction
from dataclasses import dataclass
warnings.filterwarnings("ignore")
TRAIN_FILE = "heart.csv"
TEST_FILE_FOR_PREDICTION = "x_test.csv"

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

@dataclass
class Model:
    name: str
    about: str

def pipeline(input_data_path, config_path, result_path):
    heart_data = read_process_data(input_data_path + "/" + TRAIN_FILE)
    x_train, x_val, y_train, y_val = split_train_val_data(heart_data)
    logger.info(f"Train data.shape is {x_train.shape}")
    logger.info(f"Test data.shape is {x_val.shape}")
    logger.info("Calculating model...")
    with open(config_path) as file:
        documents = yaml.full_load(file)
    logger.info(f"Loading config from '{config_path}'")   
    count = 0
    for model in documents['used_models']:

        model_data = Model(model['name'], model['about'])
        model_current = build_model(model_data.name, x_train, y_train)
        logger.info(f"Calculating score results...")
        validation(model_current, model_data.about, x_train, x_val, y_train, y_val)
        prediction(model_current, result_path, model_data.about, input_data_path + "/" + TEST_FILE_FOR_PREDICTION)
        return validation(model_current, model_data.about, x_train, x_val, y_train, y_val)
        

@click.command(name="pipeline")
@click.argument("data_path", default='ml_project/data')
@click.argument('config_path', default = 'ml_project/config/config.yml')
@click.argument('result_path', default = 'ml_project/results')
def train_pipeline_command(data_path: str, config_path: str, result_path: str):
    pipeline(data_path, config_path, result_path)


if __name__ == "__main__":
    train_pipeline_command()
