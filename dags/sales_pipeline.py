from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    load_data = BashOperator(
        task_id="load_csv",
        bash_command="python ../scripts/load_csv.py"
    )

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="""
        cd .. &&
        cd dbt_project &&
        dbt run --profiles-dir .
        """
    )

    load_data >> run_dbt