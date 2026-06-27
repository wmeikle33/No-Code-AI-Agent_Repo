def create_dag():
    dag = DAG(
        dag_id=dag_id,
        schedule=schedule,
        default_args=default_args,
        catchup=False
    )
    
    with dag:
        # Define tasks within the function
        task1 = BashOperator(
            task_id='echo_something',
            bash_command='echo "Running DAG: {{ dag.dag_id }}"'
        )
        
    return dag
