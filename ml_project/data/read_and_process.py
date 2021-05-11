import pandas as pd
import numpy as np
import scipy.stats as stats
import sys
import logging
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


def read_process_data(path_to_file):
    logger.info(f"Reading data from given path '{path_to_file}'")
    heart_data = pd.read_csv(path_to_file)
    return heart_data

def split_train_val_data(heart_data):
    x = heart_data.drop('target',axis=1)
    y = heart_data.target
    return train_test_split(x, y, test_size=0.2 , random_state = 42 , stratify = y)


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)
