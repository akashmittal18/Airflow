from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# Define your DAG configuration:
default_args = {
    'owner': 'admin',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# Create an instance of the DAG:

dag =  DAG(
    dag_id='abcd',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily'
)
#Define your tasks using operators:


task1 = BashOperator(
  task_id='first_task',
  bash_command="echo hello world, this is the first task!",
  dag=dag,
)
task2 = BashOperator(
  task_id='second_task',
  bash_command="echo hey, I am task2 and will be running after task1!",
  dag=dag,
)
task3 = BashOperator(
  task_id='thrid_task',
  bash_command="echo hey, I am task3 and will be running after task1 at the same time as task2!",
  dag=dag,
)
task4 = BashOperator(
  task_id='fourth_task',
  bash_command="echo hey, I am task4 and will be running after task2",
  dag=dag,
)
task5 = BashOperator(
  task_id='fifth_task',
  bash_command="echo hey, I am task5 and will be running after task3",
  dag=dag,
)
task6 = BashOperator(
  task_id='sixth_task',
  bash_command="echo hey, I am task6 and will be running after task2",
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
task2 >> [task4, task6]
task3 >> task5
