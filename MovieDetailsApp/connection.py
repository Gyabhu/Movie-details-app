import psycopg2


# Database name may vary.
def est_conn():
    conn = psycopg2.connect(database = 'projectcrud',user = 'postgres',password ='password',host = '127.0.0.1',port ='5432',)
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor