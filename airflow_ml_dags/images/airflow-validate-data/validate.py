import os
import pandas as pd
import json
import click
import pickle
from sklearn.metrics import f1_score


@click.command("validate")
@click.option("--input-dir")
@click.option("--output-dir")
def validate(input_dir: str, output_dir):
    val_data = pd.read_csv(os.path.join(input_dir, "val_data.csv"))
    file = open(os.path.join(output_dir, 'model.pkl'), 'rb') 
    model = pickle.load(file)
    y = val_data['target']
    val_data.drop('target', axis=1, inplace=True)
    accuracy = model.score(val_data, y)
    f1_sco = f1_score(y, model.predict(val_data), average='micro')
    metrics = {"accuracy" : accuracy, "f1_score": f1_sco}
    os.makedirs(output_dir, exist_ok=True)
    with open (os.path.join(output_dir, "metrics.json"), 'w') as f:
        json.dump(metrics, f)

if __name__ == '__main__':
    validate()