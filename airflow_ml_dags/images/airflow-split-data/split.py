import os
import pandas as pd
import click
from sklearn.model_selection import train_test_split


@click.command("split")
@click.option("--input-dir")
@click.option("--output-dir")
def split(input_dir: str, output_dir):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    #train_data = data.head(int(len(data)/4*3))
    #val_data = data.tail(int(len(data)/4))
    train_data, val_data = train_test_split(data, test_size = 0.2, shuffle = True)
    os.makedirs(output_dir, exist_ok=True)
    train_data.to_csv(os.path.join(output_dir, "train_data.csv"), index=False)
    val_data.to_csv(os.path.join(output_dir, "val_data.csv"), index=False)

if __name__ == '__main__':
    split()