import os

def menua():
    print(" 1.Bezeroen telefonoa kontsultatu \n 2.Bezeroaren telefonoa berria gehitu \n 3.Bezeroaren telefonoa ezabatu \n 4.Irten")

def escribe_fichero(nombre, numero):
    if not os.path.exists('Ariketa3'):
        os.makedirs('Ariketa3')
    
    with open('Ariketa3/listin.txt', 'a') as fichero:  
        fichero.write(f"{nombre}, {numero} \n") 

def leer_fichero():
    with open('Ariketa3/listin.txt', 'r') as fichero:
        return fichero.readlines()

def crear_fichero():
    if not os.path.exists('Ariketa3'):
        os.makedirs('Ariketa3')
    
    if not os.path.exists('Ariketa3/listin.txt'):
        with open('Ariketa3/listin.txt', 'w') as fichero:
            fichero.write("") 

def buscar_numero_por_nombre(nombre):
    lineas = leer_fichero()
    for linea in lineas:
        if "," in linea: 
            izena, numero = linea.split(",", 1) 
            if izena.strip().lower() == nombre.lower():
                return numero.strip() 
    return None  

def eliminar(nombre):
    lineas = leer_fichero() 
    nuevas_lineas = [] 

    for linea in lineas:
        if "," in linea:
            izena, _ = linea.split(",", 1)
            if izena.strip().lower() != nombre.lower(): 
                nuevas_lineas.append(linea)
def main():
    while True:
        menua()
        x = input("Aukeratu bat: ")
        
        if x == "1":
            crear_fichero()  
            nombre = input("Sartu bezeroaren izena numeroa jakitzeko: ")
            numero = buscar_numero_por_nombre(nombre)
            
            if numero:
                print(f"{nombre} bezeroaren telefono zenbakia: {numero}")
            else:
                print(f"{nombre} ez dago zerrendan.")
                
        elif x == "2":
            nombre = input("Sartu izena: ")
            numero = input("Sartu numeroa: ")
            escribe_fichero(nombre, numero)
            print(f"{nombre} eta bere telefono zenbakia gorde dira.")
        
        elif x == "3":
            nombre = input("Sartu bezero baten izena zenbakia ezabatzeko: ")
            eliminar(nombre)
        
        elif x == "4":
            print("Eskerrikasko menua ikusteagatik")
            break
        
        else:
            print("Aukeratutakoa ez da egokia")
            return

if __name__ == "__main__":
    main()
