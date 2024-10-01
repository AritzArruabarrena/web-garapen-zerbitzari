class kontaktuak:
    def __init__(self,izena,telefonoa,postaElektronikoa):
        self.izena = izena
        self.telefonoa = telefonoa
        self.postaElektronikoa = postaElektronikoa
        
    
    def __str__(self):
        return f"Izena: {self.izena}, Telefonoa: {self.telefonoa}, posta elektronikoa: {self.postaElektronikoa}"
    
    
class Agenda:
    def __init__(self):
        self.kontaktuak = []
        
    
    def kontaktuakgehitu(self, izena , telefonoa , postaElektronikoa):
        kontaktuberria = kontaktuak(izena,telefonoa,postaElektronikoa)
        self.kontaktuak.append(kontaktuberria)
        print(f"{izena} kontaktua gehituta")
    
    def inprimatu_kontaktua(self):
        if not self.kontaktuak:
            print("Ez dago kontakturik")
        else:
            for kontaktua in self.kontaktuak:
                print(kontaktua)
    
    def bilatu_kontaktua(self,izena):
        for kontaktu in self.kontaktuak:
            if kontaktu.izena.lower() == izena.lower():
                return kontaktu
            
    def editatu_kontaktua(self, izena):
        kontaktu = self.bilatu_kontaktua(izena)
        
        if kontaktu:
            print(f"Kontaktua aurkitu da: {kontaktu}")
            print("Aldatu nahi duzun atributua aukeratu:")
            print("1. Izena")
            print("2. Telefonoa")
            print("3. Emaila")
            aukera = input("Sartu aukeraren zenbakia: ")

            if aukera == "1":
                kontaktu.izena = input("Sartu izen berria: ")
            elif aukera == "2":
                kontaktu.telefonoa = input("Sartu telefono berria: ")
            elif aukera == "3":
                kontaktu.emaila = input("Sartu email berri bat: ")
            else:
                print("Aukera okerra.")
        else:
            print(f"{izena} izeneko kontaktua ez da aurkitu.")