FROM python:3.6
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY model/model.pkl ./model/model.pkl
COPY app.py /app.py

WORKDIR .

ENV PATH_TO_MODEL="/model.pkl"

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
