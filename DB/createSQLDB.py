import sqlite3


'''create an liteSQL DB file to store the decisions and can be queried later '''


def create_decision_DB():
    con = sqlite3.connect('''parkinglotDB.db''')
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE decision
                   (plate_num int, enter text, code varchar(255) , last_two varchar(255), time_stamp TIMESTAMP)''')


create_decision_DB()