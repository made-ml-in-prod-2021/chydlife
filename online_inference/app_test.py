import pickle
import pandas as pd
import numpy as np
from fastapi.testclient import TestClient
from app import app
import requests

client = TestClient(app)

def test_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200


def test_error():
    with TestClient(app) as client:
        response = client.get("/something_not_known")
        assert response.status_code == 404


def test_result():
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
    data = pd.read_csv("data/x_test.csv")
    prediction = model.predict(data)
    assert prediction is not None
    assert len(prediction) == len (data)


def test_predict():
    with TestClient(app) as client:
        response = client.get("/predict")
        data = pd.read_csv("data/x_test.csv")
        request_features = list(data.columns)
        for i in range(data.shape[0]):
            request_data = [
                x.item() if isinstance(x, np.generic) else x for x in data.iloc[i].tolist()
            ]
            response = client.get("/predict",
                json={"data": [request_data], "features": request_features},
            )
            assert response.status_code == 200

        