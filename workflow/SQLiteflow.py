


def insert_row_to_DB(Dbconection, qury):
    cur = Dbconection.cursor()
    cur.execute(qury)
    Dbconection.commit()
    return cur


def get_data_fromDB(Dbconection, qury):
    cur = Dbconection.cursor()
    cur.execute(qury)
    rows = cur.fetchall()
    return rows


def delete_all_rows(Dbconection):
    cur = Dbconection.cursor()
    cur.execute(f'''DELETE FROM decision;''')
    Dbconection.commit()
    return cur


def decision_to_SQL_qury(decision):
    qury = f"INSERT INTO decision (plate_num,enter,code,last_two,time_stamp) VALUES ({decision['plate_num']},'{decision['enter']}','{decision['code']}','{decision['last_two']}','{decision['time_stamp']}')"
    return qury



