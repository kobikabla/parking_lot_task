from main import *
from utils.ptoject_root import get_project_root
from workflow.SQLiteflow import get_data_fromDB, delete_all_rows

x = input('do you want to run check for all license plate in the images folder? y/n: \n')
if x =='y':
    run_for_all_images_in_folder(folder=f'{get_project_root()}/images',DB_connection=DB_connection())

qury = input('to serch the DB enter an SQL qury:')
data =get_data_fromDB(Dbconection=DB_connection(),qury=qury)
print('qoury data from the DB',data)
