import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

def read_process_data(path_to_file):
    heart_data = pd.read_csv(path_to_file)

def predict_model(model, x_train, y_train):
    model_used = model()
    model_used.fit(x_train, y_train)
    score(model_used, x_train, y_train)

def score(model, x_train, y_train):
    print('Train result : ')
    print('=='*20)
    print('score for data train : ', log_model.score(x_train , y_train)*100 ,'%')
    print('=='*20)
    y_pred = model.predict(x_train)
    report = classification_report(y_train,y_pred)
    print(report)
    print('=='*20)
    
    print('Test result : ')
    print('=='*20)
    print('score for data test ', log_model.score(x_test , y_test)*100,'%')
    print('=='*20)
    y_pred = model.predict(x_test)
    report = classification_report(y_test,y_pred)
    print(report)

