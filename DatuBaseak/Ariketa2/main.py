import mysql.connector
from tablak import *

def konexioa():
    dbConnect = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Admin123',
        'database': 'ariketa2'
    }
    return mysql.connector.connect(**dbConnect)

def main():
    conectar = konexioa()
    tablak(conectar)



if __name__ == "__main__":
    main()