class bezeroa:
    def __init__(self, izena, abizena, diruKopurua=0):
        self.izena = izena
        self.abizena = abizena
        self.diruKopurua = diruKopurua
        
    
    def __str__(self):
        return f"Izena: {self.izena}, abizena: {self.abizena}, diru kopurua: {self.diruKopurua}"


class bankua:
    def __init__(self):
        self.bezeroak = []
        self.egunekoDirua = 0
        
    
    