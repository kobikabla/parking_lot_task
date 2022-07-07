from utils.mongo_connection import *
from pymongo import MongoClient
from utils import mongoDB_cred
import pytest


def insert_to_DB(mongoDB_connection, qaury: dict):
    collection = mongoDB_connection
    collection.insert_one(qaury)
    return collection


def get_from_DB(mongoDB_connection, qaury: dict):
    collection = mongoDB_connection
    results = collection.find(qaury)
    r=[]
    for result in results:
        r.append(result)
    return r


def write_decision_to_DB(mongoDB_connection, decision: dict):
    insert = insert_to_DB(mongoDB_connection, qaury=decision)
    return insert


def truncat_db(mongoDB_connection):
    collection = mongoDB_connection()
    collection.delete_many({})




