import numpy as np
import pandas as pd
import requests
REQUEST_ADD = "http://127.0.0.1:8000/predict/"


if __name__ == "__main__":
    data = pd.read_csv("x_test.csv")
    request_features = list(data.columns)
    for i in range(data.shape[0]):
        request_data = [
            x.item() if isinstance(x, np.generic) else x for x in data.iloc[i].tolist()
        ]
        response = requests.get(
            REQUEST_ADD,
            json={"data": [request_data], "features": request_features},
        )
        print(response.status_code)
        print(response.json())