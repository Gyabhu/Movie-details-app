import json
from connection import est_conn

def ask_pwd(pwd,id):
    cursor = est_conn()
    sql = f'''
        INSERT INTO PASSWORD (PASSWORD,ID) VALUES('{pwd}','{id}')'''
    cursor.execute(sql)
    print("Sucess!")

    return True