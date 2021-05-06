import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from utils import read_process_data, score, predict_model


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def pipeline(input_data_path):
    logger.info(f"start train pipeline with params {training_pipeline_params}")
    heart_data = read_process_data(input_data_path)
    logger.info(f"data.shape is {data.shape}")
    train_df, val_df = split_train_val_data(
        data, training_pipeline_params.splitting_params
    )
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df.shape}")
    x = heart_data.drop('target',axis=1)
    y = heart_data.target
    x_train , x_test , y_train , y_test = train_test_split( x , y , test_size=0.2 , random_state = 42 , stratify = y)


    #transformer = build_transformer(training_pipeline_params.feature_params)
    #transformer.fit(train_df)
    #train_features = make_features(transformer, train_df)
    #train_target = extract_target(train_df, training_pipeline_params.feature_params)

    logger.info(f"train_features.shape is {train_features.shape}")

    return np.mean(val_loss), np.mean(real_val_loss)

def predict():


    return predictions

def train():


if __name__ == "__main__":
    pipeline('')