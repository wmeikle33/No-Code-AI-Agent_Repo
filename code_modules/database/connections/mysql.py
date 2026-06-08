import mysql.connector
from mysql.connector import Error

def mysql_connector():
  try:
      # Initialize the database connection session
      connection = mysql.connector.connect(
          host="localhost",       # Server IP or "localhost" for local instances
          user="your_username",   # Your MySQL database user
          password="your_password", # Your MySQL database password
          database="your_database_name" # Name of the target schema
      )
  
      if connection.is_connected():
          print("Successfully connected to the MySQL database!")
          
          # Create a cursor object to execute queries
          cursor = connection.cursor()
          
          # Execute a dummy test statement
          cursor.execute("SELECT VERSION();")
          
          # Capture the output from the cursor structure
          db_version = cursor.fetchone()
          print(f"Database Server Version: {db_version[0]}")
  
  except Error as e:
      # Handle database and connection errors gracefully
      print(f"An error occurred while connecting to MySQL: {e}")
  
  finally:
      # Ensure connections are cleaned up and closed properly
      if 'connection' in locals() and connection.is_connected():
          cursor.close()
          connection.close()
          print("MySQL database connection successfully closed.")
