import os
import pandas as pd
import click
import pickle
from sklearn.linear_model import LogisticRegression


@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir):
    train_data = pd.read_csv(os.path.join(input_dir, "train_data.csv"))
    y = train_data['target']
    train_data.drop('target', axis=1, inplace=True)
    # do something instead
    model = LogisticRegression()
    model.fit(train_data, y)
    os.makedirs(output_dir, exist_ok=True)
    with open (os.path.join(output_dir, "model.pkl"), 'wb') as f:
        pickle.dump(model, f)
if __name__ == '__main__':
    train()