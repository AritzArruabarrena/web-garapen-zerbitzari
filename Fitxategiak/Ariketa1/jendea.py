class Pertsona:
    def __init__(self, id, izena, abizena, jaiotze_data):
        self.id = id
        self.izena = izena
        self.abizena = abizena
        self.jaiotze_data = jaiotze_data
    
    def __str__(self):
        return f"ID: {self.id}, Izena: {self.izena}, Abizena: {self.abizena}, Jaiotze data: {self.jaiotze_data}"
    
    