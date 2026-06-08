import os
import mysql.connector
from mysql.connector import Error


def create_mysql_connection():
    """
    Creates a connection to a MySQL database using environment variables.
    """

    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            port=os.getenv("MYSQL_PORT", "3306"),
            database=os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"MySQL connection failed: {e}")
        return None
