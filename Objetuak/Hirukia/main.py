from hirukia import hirukia

def main():
    try:
        hirukia1 = hirukia(8,5,5)
        hirukia1.alde_handiena()
        hirukia1.triangelu_mota()
        
    
    except ValueError as ve:
        print(f"Salbuespena detektatua: {ve}")  
       
    
    

if __name__ == "__main__":
    main()
        
    