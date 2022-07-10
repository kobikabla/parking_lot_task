import configuration.dataConfig
from main import valedate_plate_num, main_flow
from workflow.SQLiteflow import get_data_fromDB
from utils.sqlite3_DB_connection import db_connection_fixture

class TestParkingLotTest:
    def test_decsion_true(self):
        decsion = valedate_plate_num(file_name='../images/license_13.jpg')
        assert decsion['enter']==True ,'the result should be enter=True last 2 digits 26'

    def test_decsion_false(self):
        decsion = valedate_plate_num(file_name='../images/license_8.jpg')
        assert decsion['enter']==False , 'the result should be enter=False last 2 digits 88'

    def test_DB_register(self,db_connection_fixture):
        main_flow(file_name='../images/license_8.jpg',DBconection=db_connection_fixture)
        decision= get_data_fromDB (Dbconection=db_connection_fixture , qury='SELECT * FROM decision WHERE plate_num=8888888 ')
        assert decision[0][1]=='False' , 'the result should be enter=False last 2 digits 88 tests the result in the DB'

