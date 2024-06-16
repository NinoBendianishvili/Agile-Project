
FROM apache/airflow:2.8.1


ENV AIRFLOW_HOME=/opt/airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags /opt/airflow/dags




USER airflow
