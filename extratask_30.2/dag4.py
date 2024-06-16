from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id = "sales_weather_model_pipeline",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

def pick_erp_system():
    print("pick erp system")

def fetch_sales_old():
    print("fetch sales old")

def fetch_sales_new():
    print("fetch sales new")

def fetch_weather():
    print("fetch weather")

def clean_sales_old():
    print("clean sales old")

def clean_sales_new():
    print("clean sales new")

def clean_weather():
    print("clean weather")

def join_datasets():
    print("join datasets")

def train_model():
    print("train model")

def deploy_model():
    print("deploy model")


pick_erp_system_task = PythonOperator(task_id='pick_erp_system', python_callable=pick_erp_system, dag=dag)
fetch_sales_old_task = PythonOperator(task_id='fetch_sales_old', python_callable=fetch_sales_old, dag=dag)
fetch_sales_new_task = PythonOperator(task_id='fetch_sales_new', python_callable=fetch_sales_new, dag=dag)
fetch_weather_task = PythonOperator(task_id='fetch_weather', python_callable=fetch_weather, dag=dag)
clean_sales_old_task = PythonOperator(task_id='clean_sales_old', python_callable=clean_sales_old, dag=dag)
clean_sales_new_task = PythonOperator(task_id='clean_sales_new', python_callable=clean_sales_new, dag=dag)
clean_weather_task = PythonOperator(task_id='clean_weather', python_callable=clean_weather, dag=dag)
join_datasets_task = PythonOperator(task_id='join_datasets', python_callable=join_datasets, dag=dag)
train_model_task = PythonOperator(task_id='train_model', python_callable=train_model, dag=dag)
deploy_model_task = PythonOperator(task_id='deploy_model', python_callable=deploy_model, dag=dag)

pick_erp_system_task >> [fetch_sales_old_task, fetch_sales_new_task, fetch_weather_task]
fetch_sales_old_task >> clean_sales_old_task
[fetch_sales_new_task, clean_sales_old_task] >> clean_sales_new_task
fetch_weather_task >> clean_weather_task
[clean_sales_old_task, clean_sales_new_task, clean_weather_task] >> join_datasets_task
join_datasets_task >> train_model_task >> deploy_model_task

