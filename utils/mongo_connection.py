from pymongo import MongoClient

from configuration import dataConfig
from utils import mongoDB_cred
import pytest



@pytest.fixture(scope="class")
def mongoDB_connection():
    CONNECTION_STRING = f"mongodb+srv://kobi_k:{mongoDB_cred.password}@cluster0.dyihicq.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    DB = client[dataConfig.collectnion]
    yield DB[dataConfig.DBname]
    truncat_db(mongoDB_connection=DB[dataConfig.DBname])

""" connection to mongodb data base
    :param DBname: table name
    :param collectnion: Is the mongodb cllection for that progect (set to 'parking_lot' by default)  
    :return: the connection to the DB.
    """

def mongoDB_connection_def():
    CONNECTION_STRING = f"mongodb+srv://kobi_k:{mongoDB_cred.password}@cluster0.dyihicq.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    DB = client[dataConfig.collectnion]
    return DB[dataConfig.DBname]



def truncat_db(mongoDB_connection):
    collection = mongoDB_connection
    collection.delete_many({})


