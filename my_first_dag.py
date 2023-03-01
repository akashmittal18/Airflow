from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define your DAG configuration:

default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2023, 2, 27),
    'email': ['admin'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create an instance of the DAG:

dag = DAG(
    'my_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

#Define your tasks using operators:

task1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

task2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

task3 = BashOperator(
    task_id='echo',
    depends_on_past=False,
    bash_command='echo "hello world"',
    retries=3,
    dag=dag,
)

#Define the order of the tasks by setting up their dependencies:

task1 >> [task2, task3]
