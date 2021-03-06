import sqlite3

import pytest

import configuration.dataConfig
from utils.ptoject_root import get_project_root

from workflow.SQLiteflow import delete_all_rows, get_data_fromDB


@pytest.fixture(scope="class")
def db_connection_fixture():
    con = sqlite3.connect(f'{get_project_root()}/DB/parkinglotDB.db')
    print(f'{get_project_root()}/DB/parkinglotDB.db')
    yield con
    '''teardown after all tests (delete all rows from DB and) and close connection'''
    delete_and_close_DB(con)


def DB_connection():
    con = sqlite3.connect(f'{get_project_root()}/DB/parkinglotDB.db')
    return con



def delete_and_close_DB(DB_connection):
    # Save (commit) the changes
    delete_all_rows(DB_connection)
    # close connection
    DB_connection.close()

