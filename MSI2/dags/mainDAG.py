from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from image_loader import fetch_image_from_url
from quote_loader import fetch_quote
from main import send_to_teams

teams_webhook_url = "https://quantorillc.webhook.office.com/webhookb2/986a3528-9d9c-43aa-a313-28f621c59260@124ccfbd-07ea-44e3-8794-af8986d63809/IncomingWebhook/c314d4a9c25a47db931489749aa7d788/dfc6f754-1356-49de-9d68-a09d53f86f85"
local_tz = pendulum.timezone("America/New_York")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    dag_id="agile_project_MSI_2",
    description="DAG to send daily quote and image to Teams",
    start_date=days_ago(1),  # Start from yesterday to avoid immediate execution upon creation
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    tags=["MSI2", "daily"],
) as dag:

    def fetch_and_send_to_teams(**kwargs):
        image_url = "https://picsum.photos/200/300"
        image_data = fetch_image_from_url(image_url)
        if image_data:
            quote = fetch_quote()
            if quote:
                send_to_teams(teams_webhook_url, quote=quote, author="Anonymous", image_url=image_url)

    load_quote_task = PythonOperator(
        task_id="load_quote",
        python_callable=fetch_quote,
        provide_context=True,
    )

    load_image_task = PythonOperator(
        task_id="load_image",
        python_callable=fetch_image_from_url,
        provide_context=True,
    )

    send_to_teams_task = PythonOperator(
        task_id="send_to_teams",
        python_callable=send_to_teams,
        provide_context=True,
    )

    load_quote_task.set_downstream(load_image_task)
    load_image_task.set_downstream(send_to_teams_task)
