
from authorized import authorized
from connection import est_conn

@authorized
def create():

    id = int(input("Enter your id: "))
    name = input("Enter your name: ")
    movie = input("Movie title: ")
    cursor = est_conn()
    sql = f"""
        INSERT INTO MYMOVIES(ID,NAME,MOVIES) VALUES ('{id}','{name}','{movie}')
        """
    cursor.execute(sql)

    cont = input(f"Congratulations {movie} has been registered! Continue? (y/n) ")
    return True if cont.lower() =='y' else False
