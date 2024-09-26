class pertsona:
    def __init__(self,izena,adina):
        try:
            self.izena = izena
            self.adina = int(adina)
            if not (self.adina > 0):
                raise ValueError("Adina ezin da 0 baino txikiagoa izan")
        except ValueError as e:
            print(f"Errorea: {e}")
            raise
    
    def imprimatu(self):
        print(f"Pertsonaren izena: {self.izena}")
        print(f"Pertsonaren adina: {self.adina}")
        
    
    def adinnagusia(self):
        try:
            if self.adina >= 18:
                print(f"{self.izena} 18 urte baino gehiago ditu")
            
            else:
                print(f"{self.izena} , 18 urte baino gutxiago ditu")       
        except Exception as e:
            print(f"Errorea emaitza kalkulatzerakoan: {e}")
        