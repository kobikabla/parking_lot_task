import os

from rules import valedate_plate_num
from utils.sqlite3_DB_connection import DB_connection
from workflow.SQLiteflow import decision_to_SQL_qury, insert_row_to_DB




def main_flow(file_name,DBconection):
    decision = valedate_plate_num(file_name=file_name)
    # write_decision_to_DB(mongoDB_connection=mongoDB_connection ,decision=decision)
    insert_row_to_DB(Dbconection=DBconection, qury=decision_to_SQL_qury(decision))



def run_for_all_images_in_folder(folder,DB_connection):
    for file in os.listdir(folder):
        main_flow(file_name=f'{folder}/{file}',DBconection=DB_connection)


run_for_all_images_in_folder(folder='./images',DB_connection=DB_connection())

