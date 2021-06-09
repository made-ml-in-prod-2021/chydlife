import os

import click
from sklearn.datasets import load_wine


@click.command("download")
@click.argument("output_dir")
def download(output_dir: str):
    data_input = load_wine(as_frame=True)
    data_pd = data_input['data']
    data_pd['target'] = data_input['target']
    os.makedirs(output_dir, exist_ok=True)
    data_pd.to_csv(os.path.join(output_dir, "data.csv"), index=False)


if __name__ == '__main__':
    download()