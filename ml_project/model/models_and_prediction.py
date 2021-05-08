import pandas as pd
import numpy as np
import scipy.stats as stats
import sys
import yaml
import logging
import warnings
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings("ignore")


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def build_model(model, x_train, y_train):
    logger.info(f'Current model name: {model}')
    if model == "LogisticRegression":
        current_model = LogisticRegression()
    elif model == "RandomForestClassifier":
        current_model = RandomForestClassifier()
    else:
        raise NotImplementedError()
    model_used = current_model.fit(x_train, y_train)
    return model_used


def validation(model, description, x_train, x_test, y_train, y_test):
    logger.info(f'Train result : {description}')
    logger.info('=='*20)
    logger.info(f"Score for data train: {model.score(x_train , y_train)*100}%")
    logger.info('=='*20)
    y_pred = model.predict(x_train)
    report = classification_report(y_train,y_pred)
    logger.info(report)
    logger.info('=='*20)
    logger.info(f'Test result : {description}')
    logger.info('=='*20)
    logger.info(f"score for data test: {model.score(x_test , y_test)*100}%")
    logger.info('=='*20)
    y_pred = model.predict(x_test)
    report = classification_report(y_test,y_pred)
    logger.info(report)
    return model.score(x_train , y_train)*100, model.score(x_test , y_test)*100


def prediction(model_current, result_path, model_name, path_x_test):
    x_test = pd.read_csv(path_x_test)
    result = model_current.predict(x_test)
    with open(result_path + " "+ model_name, 'w') as out_file:
        out_file.write(str(result))
    logger.info(f'Prediction file has been created for {model_name} model')