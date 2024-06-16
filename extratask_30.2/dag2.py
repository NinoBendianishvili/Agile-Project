from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

start_time = datetime.strptime('11:00', '%H:%M')
end_time = datetime.strptime('19:00', '%H:%M')
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    dag_id="hourly_working_hours_dag",
    start_date=datetime(2024, 6, 15),
    schedule_interval='0 */2 * * 1-5', 
    default_args=default_args,
) as dag:
    def hourly_task():
        print("Executing hourly task")
    hourly_task_op = PythonOperator(
        task_id="hourly_task",
        python_callable=hourly_task,
    )

  
    hourly_task_op

