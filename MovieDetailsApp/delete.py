from connection import est_conn


def delete(id):

    cursor = est_conn()
    sql = f'''
        DELETE FROM MYMOVIES WHERE ID = '{id}'

        '''
    cursor.execute(sql)
    print("Information Deleted!")

    cont = input("Sucessfully deleted, Continue? Y/N: ")
    return True if cont.lower()=='y' else False