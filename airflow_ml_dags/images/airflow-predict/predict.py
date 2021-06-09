import os
import pandas as pd
import pickle
import click


@click.command("predict")
@click.option("--input-dir")
@click.option("--model_path")
@click.option("--output-dir")
def predict(input_dir: str, model_path: str,output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    file = open(os.path.join(model_path, 'model.pkl'), 'rb') 
    model = pickle.load(file)
    data.drop('target', axis=1, inplace=True)
    result = model.predict(data)
    os.makedirs(output_dir, exist_ok=True)
    result.to_csv(os.path.join(output_dir, "predictions.csv"),index=False)
if __name__ == '__main__':
    predict()