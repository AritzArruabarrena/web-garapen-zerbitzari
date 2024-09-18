import os

def menua():
    print(" 1.Bezeroen telefonoa kontsultatu \n 2.Bezeroaren telefonoa berria gehitu \n 3.Bezeroaren telefonoa ezabatu \n 4.Irten")

def escribe_fichero(nombre, numero):
    # Crear el directorio si no existe
    if not os.path.exists('Ariketa3'):
        os.makedirs('Ariketa3')
    
    # Añadir el nombre y número al fichero
    with open('Ariketa3/listin.txt', 'a') as fichero:  # 'a' para añadir
        fichero.write(f"{nombre}, {numero} \n")  # Añadir nombre y número separados por coma

def leer_fichero():
    # Leer todas las líneas del fichero
    with open('Ariketa3/listin.txt', 'r') as fichero:
        return fichero.readlines()  # Devolver las líneas en forma de lista

def crear_fichero():
    # Crear el directorio si no existe
    if not os.path.exists('Ariketa3'):
        os.makedirs('Ariketa3')
    
    # Crear el fichero si no existe
    if not os.path.exists('Ariketa3/listin.txt'):
        with open('Ariketa3/listin.txt', 'w') as fichero:
            fichero.write("")  # Crear un fichero vacío

def buscar_numero_por_nombre(nombre):
    # Buscar el número de teléfono correspondiente a un nombre
    lineas = leer_fichero()
    for linea in lineas:
        if "," in linea:  # Comprobar que la línea tiene el formato correcto
            izena, numero = linea.split(",", 1)  # Dividir en nombre y número (solo una coma)
            if izena.strip().lower() == nombre.lower():  # Comparar nombres ignorando mayúsculas
                return numero.strip()  # Devolver el número sin espacios extra
    return None  # Si no se encuentra el nombre

def main():
    while True:
        menua()
        x = input("Aukeratu bat: ")
        
        if x == "1":
            crear_fichero()  # Asegurarse de que el fichero existe
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
            print("Hola3")
        
        elif x == "4":
            print("Eskerrikasko menua ikusteagatik")
            break
        
        else:
            print("Aukeratutakoa ez da egokia")
            return

if __name__ == "__main__":
    main()
