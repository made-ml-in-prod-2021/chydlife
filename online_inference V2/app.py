import logging
import os
import pickle
from typing import List, Union, Optional
import sys
import numpy as np
import pandas as pd
import uvicorn
import time
from fastapi import FastAPI
from pydantic import BaseModel, conlist
from sklearn.pipeline import Pipeline
PATH_TO_MODEL = "model/model.pkl"

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


class ClassRequest(BaseModel):
    
    data: List[conlist(Union[float, int])]
    features: List[str]

class ClassResponse(BaseModel):

    cls_id: int


def load_object(path: str) -> Pipeline:
    logger.info("Uploading file ...")
    with open(path, "rb") as f:
        return pickle.load(f)


def make_predict(
    data: List, features: List[str], model: Pipeline,
) -> List[ClassResponse]:
    data = pd.DataFrame(data, columns = features)
    predicts = model.predict(data)
    print (predicts)
    return [
        ClassResponse(cls_id=cls_id) for cls_id in predicts
    ]


app = FastAPI()


@app.get("/")
def main():
    return "it is entry point of our predictor"


@app.on_event("startup")
def load_model():
    global model
    time.sleep(20)
    model_path = PATH_TO_MODEL
    print (model_path)
    if model_path is None:
        err = f"PATH_TO_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)

    model = load_object(model_path)
    #time.sleep(60)
    #raise OSError("Application stop")

@app.get("/healz")
def health() -> bool:
    return not (model is None)


@app.get("/predict/", response_model=List[ClassResponse])
def predict(request: ClassRequest):
    return make_predict(request.data, request.features, model)


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=os.getenv("PORT", 8000))