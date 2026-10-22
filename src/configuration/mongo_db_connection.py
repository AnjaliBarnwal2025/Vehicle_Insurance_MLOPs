import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout error when connectig to MongoDB
ca=certifi.where()

class MongoDBClient:
    """
    MongoDBClient is reponsible for establishing a connection to the MongoDB database.

    Attributes:
    ------------
    client: MongoClient
        A shared MongoClient 
    database: Database
        The specific database instance that MongoDB client connects to.
    
    Methods:
    ------------
    __init__(database_name: str)->None
        initializes the mongoDB connection using the given database name
    """
    client=None #Shared MongoClient instance across all mongoDB 

    def __init__(self, database_name: str = DATABASE_NAME)->None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters:
        -------------
        database_name: str, optional
            Name of the MongoDB database to connect to. Defualt is set by DATABASE_NAME constant.

        Raises:
        ------------
        MyException
            If there is an issue in connecting to MongoDB or if the environment variable for the MongoDB URL is not set.  
        """
        try:
            # Check if a MongoDB connection has already been established; if not then create a new one
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment Variable {MONGODB_URL_KEY} is not set.")

                # Establish a new MongoDB client connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)

            # Use the shared MongoClient for this instance
            self.client=MongoDBClient.client
            self.database=self.client[database_name] # Connect to the specified database
            self.database_name=database_name
            logging.info("MongoDB Connection successful.")

        except Exception as e:
            # Raise a custome exception with traceback details if connection fails
            raise MyException(e,sys)