import mysql.connector
from tablak import *

def konexioa():
    dbConnect = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Admin123',
        'database': 'ariketa1'
    }
    return mysql.connector.connect(**dbConnect)

def main():
    conectar = konexioa()
    try:
        tablak(conectar)
    except:
        pass 
    #datuak_bete(conectar)
    # try:
    #     taulak_ezabatu(conectar)
    # except Exception as e:
    #     print(f"Error dropping tables: {e}")
    # conectar.close()
    datuak_ezabatu(conectar)
    
    

if __name__ == "__main__":
    main()
