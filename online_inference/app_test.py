import pickle
import pandas as pd
from fastapi.testclient import TestClient
from app import app


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

        