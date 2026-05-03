"""
Example DAG with only dummy tasks (no external systems).

Run Airflow from the `airflow/` directory using `start_standalone.sh`.
"""

from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


def _log_dummy() -> None:
    print("dummy_python_log: no-op task completed")


with DAG(
    dag_id="dummy_linear_pipeline",
    description="Linear dummy pipeline for local Airflow smoke testing.",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["dummy", "example"],
) as dag:
    start = EmptyOperator(task_id="start")
    fetch = EmptyOperator(task_id="dummy_fetch")
    transform = EmptyOperator(task_id="dummy_transform")
    log = PythonOperator(task_id="dummy_python_log", python_callable=_log_dummy)
    load = EmptyOperator(task_id="dummy_load")
    end = EmptyOperator(task_id="end")

    start >> fetch >> transform >> log >> load >> end
