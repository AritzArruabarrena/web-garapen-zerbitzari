class hirukia:
    def __init__(self,a,b,c):
        
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Aldeek positiboa izan behar dute")
        
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Ezin da triangelu bat sortu emandako aldeekin.")
        
        self.a = a
        self.b = b
        self.c = c
    
    
    def alde_handiena(self):
        max_aldea = max(self.a, self.b, self.c)
        print(f"Triangeluaren alde handiena: {max_aldea}")
        
    
    
    def triangelu_mota(self):
        if self.a == self.b == self.c:
            print("Triangelua aldeberdina da.")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Triangelua isoszelea da.")
        else:
            print("Triangelua eskalenoa da.")