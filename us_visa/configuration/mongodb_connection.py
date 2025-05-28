import os
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGO_DB_KEY
import sys
import pymongo
import certifi

ca=certifi.where()

class MongoDBClient:
    client=None

    def __init__(self,database_name=DATABASE_NAME)->None:
        try:
            if MongoDBCLient.client is None:
                mongo_db_url=os.getenv(MONGO_DB_KEY)
                if mongo_db_url is None:
                    raise Exception(f" Environment Key: {MONGO_DB_KEY} is not set")

                MongoDBClient.client=pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)

            self.client=MongoDBClient.client
            self.database=self.client[database_name]
            self.database_name=database_name
            logging.info("MongoDB connection succesfull")

        except Exception as e:
            raise USvisaException(e,sys)

