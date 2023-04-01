from connection import est_conn
def authorized(func):
    def inner(*args,**kwargs):
        cursor = est_conn()
        sql = f'''SELECT PASSWORD FROM PASSWORD WHERE ID = '1'
                '''
        cursor.execute(sql)
        password = cursor.fetchone()
        pwd = input("Enter Password: ")
        if pwd == password[0]:
            return func(*args,**kwargs)
        else:
            print("Not Authorised")
    return inner
