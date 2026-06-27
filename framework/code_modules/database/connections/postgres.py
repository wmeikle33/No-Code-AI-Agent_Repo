import os
import psycopg
from psycopg import OperationalError

def postgres_connection(connection_string: str) -> psycopg.Connection | None:
    """
    Establishes a connection to a PostgreSQL database.
    
    :param connection_string: The PostgreSQL connection URI or connection string.
    :return: A psycopg.Connection instance if successful, or None if it fails.
    """
    try:
        # Establish the connection
        conn = psycopg.connect(connection_string)
        
        # Verify the server is responsive by running a simple query
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print(f"Successfully connected to PostgreSQL! Server version: {db_version[0]}")
            
        return conn
        
    except OperationalError as oe:
        print(f"Operational error: Unable to connect to the server. Details: {oe}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
