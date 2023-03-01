from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Define your DAG configuration:
default_args = {
    'owner': 'akash',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# Create an instance of the DAG:
dag =  DAG(
    dag_id='our_first_dag_v1',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily'
) 
#Define your tasks using operators:
task1 = BashOperator(
  task_id='first_task',
  bash_command="echo hello world, this is the first task!"
  dag=dag,
)
task2 = BashOperator(
  task_id='second_task',
  bash_command="echo hey, I am task2 and will be running after task1!"
  dag=dag,
)
task3 = BashOperator(
  task_id='thrid_task',
  bash_command="echo hey, I am task3 and will be running after task1 at the same time as task2!"
  dag=dag,
)
  # Task dependency method 1
  # task1.set_downstream(task2)
  # task1.set_downstream(ta
  # Task dependency method 2
  # task1 >> task2
  # task1 >> t
  # Task dependency method 3
  
#Define the order of the tasks by setting up their dependencies:  
task1 >> [task2, task3]
