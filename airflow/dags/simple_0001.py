from airflow.models.dag import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

with DAG('simple_0001_1',
         max_active_runs=3,
         schedule_interval=timedelta(minutes=5),
         start_date=datetime(2020, 4, 25),
         concurrency=16,
         catchup=False) as simple_0001_1:

    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo hello',
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo hello',
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo hello',
    )

    task_4 = BashOperator(
        task_id='task_4',
        bash_command='echo hello',
    )

    task_1 >> task_2
    task_2 >> task_3
    task_3 >> task_4
