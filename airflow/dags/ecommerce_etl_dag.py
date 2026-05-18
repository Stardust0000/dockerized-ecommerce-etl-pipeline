from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id = "ecommerce_etl_pipeline",
    start_date = datetime(2026, 5, 12),
    schedule="@daily",
    catchup=False
) as dag:
    run_etl = BashOperator(
        task_id = "run_etl_pipeline",
        bash_command="python /opt/airflow/etl/main.py"
    )