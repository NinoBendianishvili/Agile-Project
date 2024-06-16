from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

start_date = datetime(2024, 6, 15)
end_date = datetime(2024, 7, 13)
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id="weekly_trigger_dag",
    start_date=start_date,
    end_date=end_date,
    schedule_interval='@weekly', 
    default_args=default_args,
) as dag:
    def weekly_task():
        print("Executing weekly task")
    weekly_task_op = PythonOperator(
        task_id="weekly_task",
        python_callable=weekly_task,
    )


    weekly_task_op

