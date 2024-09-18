import os
def menua():
    print(" 1.Bezeroen telefonoa kontsultatu \n 2.Bezeroaren telefonoa berria gehitu \n 3.Bezeroaren telefonoa ezabatu \n 4.Irten")


def escribe_fichero(mensaje):
    with open('Ariketa3/listin.txt', 'w') as fichero:
        fichero.write(str(mensaje))
    

def leer_fichero():
    with open('Ariketa3/listin.txt', 'r') as fichero:
        return fichero.read() 
        
def main():
    
    while(True):
        menua()
        x = input("Aukeratu bat:")
        
        if x == "1":
            if not os.path.exists('Ariketa3/listin.txt'):
               x = 0
            else:
                x = leer_fichero()  
        elif x == "2":
            print("Hola2")
        elif x == "3":
            print("Hola3")
        elif x == "4":
            print("Eskerrikasko menua ikusteagatik")  
            return
        else:
            print("Aukeratutakoa ez da egokia")
            return
        
        

if __name__ == "__main__":
    main()