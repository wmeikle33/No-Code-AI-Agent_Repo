import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError

def get_mongodb_client(uri: str) -> MongoClient | None:
    """
    Establishes a connection to a MongoDB instance.
    
    :param uri: The MongoDB connection string URI.
    :return: A MongoClient instance if successful, or None if the connection fails.
    """
    try:
        # Initialize the client. By default, it connects in the background.
        client = MongoClient(uri)
        
        # Force a call to verify the connection is successful
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client
        
    except ConfigurationError as ce:
        print(f"Configure error: Check your connection string format. Details: {ce}")
        return None
    except ConnectionFailure as cf:
        print(f"Server not available: {cf}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
