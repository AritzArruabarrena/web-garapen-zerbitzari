from kontaktuak import *

def menu():
    print("Menua:")
    print("1. Gehitu kontaktua")
    print("2. Inprimatu harremanetarako zerrenda")
    print("3. Bilatu kontaktua")
    print("4. Editatu kontaktua")
    print("5. Irten")
    
def main():
    agenda = Agenda()
    while True:
        menu()  
        aukera = input("Aukeratu aukera (1-5): ")
        
        if aukera == 1:
            izena = input("Sartu kontaktuaren izena: ")
            telefonoa = input("Sartu kontaktuaren telefonoa: ")
            emaila = input("Sartu kontaktuaren emaila: ")
            agenda.gehitu_kontaktua(izena, telefonoa, emaila)

        elif aukera == "2":
            agenda.inprimatu_kontaktuak()

        elif aukera == "3":
            izena = input("Sartu bilatu nahi duzun izena: ")
            kontaktua = agenda.bilatu_kontaktua(izena)
            if kontaktua:
                print(kontaktua)
            else:
                print(f"{izena} izeneko kontaktua ez da aurkitu.")

        elif aukera == "4":
            izena = input("Sartu editatu nahi duzun kontaktuaren izena: ")
            agenda.editatu_kontaktua(izena)

        elif aukera == "5":
            print("Eskerrik asko! Programatik irteten...")
            break

        else:
            print("Aukera okerra. Saiatu berriro.")
    
    
    

if __name__ == "__main__":
    main()