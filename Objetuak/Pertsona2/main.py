from pertsona import pertsona

def main():
    try:
        pertsona1 = pertsona("Aritz" , 18)
        pertsona1.imprimatu()
        pertsona1.adinnagusia()
        
        pertsona1 = pertsona("Jon" , 20)
        pertsona1.imprimatu()
        pertsona1.adinnagusia()
        
        pertsona1 = pertsona("Mikel" , 16)
        pertsona1.imprimatu()
        pertsona1.adinnagusia()
        
    except ValueError as ve:
        print(f"Salbuespena detektatua: {ve}")  
    

if __name__ == "__main__":
    main()