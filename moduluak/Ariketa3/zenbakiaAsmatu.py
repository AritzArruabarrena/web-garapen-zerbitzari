import random

def irakurri_zenbakiak( min , max):

    if min >= max:
        raise ValueError("Minimoa eta maximoa berdinak dira edo minimoa handiagoa da")
    else:
        randoma =  int(random.uniform(min,max))
        return randoma
    

def zenbakia_asmatu(zenbakia):
    
    zenbakiaR = irakurri_zenbakiak()
    
    aukerak = 0
    
    while aukerak < 7:
        
        if zenbakia < zenbakiaR:
           aukerak += 1
           print("Autasko zenbakia handiagoa da")
        elif zenbakia > zenbakiaR:
            aukerak += 1
            print("Autasko zenbakia txikiagoa da")
        else:
            print("Zorionak zenbakia asmatu duzu!")
            return True
    
    else:
        print(f"Bukatu zaizu intento kopurua. Autasko zenbakia: {zenbakiaR}")
    


def main():
    min = int(input("Sartu zenbaki txiki bat:"))
    max = int(input("Sartu zenbaki handi bat:"))
    zenbakia = int(input(f"Sartu zenbaki bat {min} eta {max} artean"))
    
    irakurri_zenbakiak(min,max)
    if min >= max:
            raise ValueError("Minimoa eta maximoa berdinak dira edo minimoa handiagoa da")

    if zenbakia_asmatu(zenbakia):
        print("Zorionak, zu re zenbakia asmatu duzu!")
    else:
        print("Saia zaitez berriro hurrengoan.")


if __name__ == "__main__":
    main()
            
        