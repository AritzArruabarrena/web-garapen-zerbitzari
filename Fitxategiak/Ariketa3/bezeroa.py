class Pertsona:
    def __init__(self, zenbakia, izena):
        self.zenbakia = zenbakia
        self.izena = izena
    
    def __str__(self):
        return f"ID: {self.zenbakia}, Izena: {self.izena}"
    
    