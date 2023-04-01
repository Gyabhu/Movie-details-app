import json

from connection import est_conn

def read(id):
    cursor = est_conn()
    sql = f'''
    SELECT * FROM MYMOVIES WHERE ID = '{id}'
    '''
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

    cont = input(f"Do you wish to view more? Continue? (y/n) ")
    return True if cont.lower() =='y' else False
