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

def menua():
    print("1.Ikasle berri bat \n 2.Notak sartu \n 3.Notak aldatu \n 4.Ikasgai berri bat sartu \n 5. Ikaslea ezabatu \n 6.Irten")
    
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
    #datuak_ezabatu(conectar)
    
    while True:
        menua()
        x = input("Aukeratu bat: ")
        
        if x == "1":
            kodea = input("Sartu ikasle kodea: ")
            izena = input("Sartu ikaslearen izena: ")
            abizena = input("Sartu ikaslearen abizena: ")
            ikaslea_sortu(conectar,kodea,izena,abizena)
            
        if x == "2":
            nota = input("Sartu nota: ")
            oharra = input("Sartu oharra: ")
            ikasle_kodea = input("Sartu ikaslearen kodea: ")
            ikasgai_kodea = input("Sartu ikasgai kodea: ")
            nota_sartu(conectar,nota,oharra,ikasle_kodea,ikasgai_kodea)
            
        if x == "3":
            nota = input("Sartu nota: ") 
            ikasle_kodea = input("Sartu ikaslearen kodea: ")
            ikasgai_kodea = input("Sartu ikasgaiaren kodea: ")
            nota_aldatu(conectar,nota,ikasgai_kodea, ikasgai_kodea)
        if x == "4":
            ikasgai_kodea = input("Sartu ikasgai kodea: ")
            izena = input("Sartu ikasgaiaren izena: ")
            maila = input("Sartu ikasgaiaren maila: ")
            hizkuntza = input("Sartu hizkuntza: ")
            gehitu_ikasgaia(conectar,ikasgai_kodea,izena,maila,hizkuntza)
        if x == "5":
            ikasle_kodea = input("Sartu ikasle kodea:")
            
            ezabatu_ikaslea(conectar,ikasle_kodea)
        if x == "6":
            print("Eskerrik Asko!") 
            break
    
    

if __name__ == "__main__":
    main()
