#fichategia berria sortu bisitak.txt  eta 0 balioa eman eta sortuta badago irakurri
#G eman ezkero +1 zenbakiari
#K eman ezkero -1 zenbakiari
#G eta K ez badira print
#Zenbakia gorde
import os

def escribe_fichero(mensaje):
    with open('Ariketa2/bisitak.txt', 'w') as fichero:
        fichero.write(str(mensaje))
       
def leer_fichero():
    with open('Ariketa2/bisitak.txt', 'r') as fichero:
        return int(fichero.read()) 

def main():
    if not os.path.exists('Ariketa2/bisitak.txt'):
        kontadorea = 0
    else:
        kontadorea = leer_fichero()
        
    x = input("Beste bat Gehitu(G) edo beste bat kendu(K)")
    if x == "G":
        kontadorea += 1
        escribe_fichero(kontadorea)
        print(leer_fichero())
                
    elif x == "K":
        kontadorea -= 1
        escribe_fichero(kontadorea)
        print(leer_fichero())
    else:
       print("G edo K bakarrik ahal dira")
        
if __name__ == "__main__":
    main()