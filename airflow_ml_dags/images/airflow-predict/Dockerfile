FROM airflow-ml-base:latest

COPY predict.py /predict.py
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "predict.py"]