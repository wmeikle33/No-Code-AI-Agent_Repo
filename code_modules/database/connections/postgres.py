def read_database(condition):
    connection = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_username",
            password="your_password",
            port="5432"
        )
      
    except (Exception, Error) as error:
        print("Error while fetching data from PostgreSQL:", error)
