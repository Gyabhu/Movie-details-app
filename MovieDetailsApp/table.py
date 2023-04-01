from connection import est_conn

cursor = est_conn()

cursor.execute("DROP TABLE IF EXISTS PROJECTCRUD")

sql = """CREATE TABLE MYMOVIES(ID VARCHAR(20),NAME VARCHAR (20),MOVIES VARCHAR(100))"""
sql2 =  """CREATE TABLE PASSWORD(ID VARCHAR(20),PASSWORD VARCHAR(20))"""
cursor.execute(sql)
cursor.execute(sql2)
print("Table created!")