import os
from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable
DATA_PATH = "/Users/mariapopova/Documents/GitHub/chydlife/airflow_ml_dags/data:/data"

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "make-new-prediction",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:

    predict = DockerOperator(
        image="airflow-preprocess",
        command="--input-dir /data/processed/{{ ds }} --output-dir /data/predictions{{ ds }} --model_path --output-dir /data/predictions{{ ds }}",
        #{Variable.get('MODEL_PATH', default_var=)}
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        volumes=[DATA_PATH]
    )

    predict
