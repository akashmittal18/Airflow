# Airflow

Airflow is an open-source platform designed to programmatically author, schedule, and monitor workflows. It allows you to create and execute complex data pipelines and workflows that can involve multiple steps, dependencies, and sources of data.

At its core, Airflow provides a way to define a DAG (Directed Acyclic Graph) of tasks, which can be orchestrated and executed on a schedule or triggered manually. Each task in the DAG represents a specific operation or step in the workflow, and tasks can depend on one another, allowing you to create complex dependencies between tasks.

Airflow Task Life Cycle

<img width="622" alt="image" src="https://user-images.githubusercontent.com/47140557/222112653-1f3d45ca-6e42-4d06-a064-67ff5e4673ba.png">


A happy workflow execution process

<img width="556" alt="image" src="https://user-images.githubusercontent.com/47140557/222113368-bd46f536-9b19-4201-9609-e8fb6fb66af8.png">

## Install Airflow on Linux
1. Install Airflow using pip

```cmd
pip install apache-airflow
```

2. Initialize Airflow database: After installing Airflow, you need to initialize its metadata database.

```cmd
airflow db init

```
3. Start Airflow webserver and scheduler: Once the database is initialized, you can start the Airflow webserver and scheduler using the following commands:
```cmd
airflow webserver --port 8080
airflow scheduler

```
```text
This will start the webserver on port 8080 and the scheduler in the background. You can now access the Airflow web UI by opening a web browser and navigating to http://localhost:8080.
```
