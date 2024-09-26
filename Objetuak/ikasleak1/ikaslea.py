class ikaslea:
    
    def __init__(self,izena,kalifikazioa):
        try:
            self.izena = izena
            self.kalifikazioa = float(kalifikazioa)
            if not (0 <= self.kalifikazioa <= 10):
                raise ValueError("Kalifikazioa 0 eta 10 bitartekoa izan behar da.")
        except ValueError as e:
            print(f"Errorea: {e}")
            raise
        
        
    def ikasleaimprimitu(self):
        print(f"Ikaslearen izena: {self.izena}")
        print(f"Kalifikazioa: {self.kalifikazioa}")
        
    
    def emaitza(self):
        try:
            if self.kalifikazioa >= 5:
                print(f"{self.izena} ikasleak GAINDITU du, {self.kalifikazioa} kalifikazioarekin.")
            else:
                print(f"{self.izena} ikasleak EZ DU GAINDITU, {self.kalifikazioa} kalifikazioarekin.")
        except Exception as e:
            print(f"Errorea emaitza kalkulatzerakoan: {e}")
    