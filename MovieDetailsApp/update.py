from connection import est_conn


def update(id,key,value):


    cursor = est_conn()

    sql = f'''
    UPDATE MYMOVIES SET {key.upper()} = '{value}' WHERE ID = '{id}'
    '''
    cursor.execute(sql)

    cont = input("Updated Sucessfully, Do you want to continue? Y/N: ")
    return True if cont.lower() =='y' else False