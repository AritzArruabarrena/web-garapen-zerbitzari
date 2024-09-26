from ikaslea import ikaslea

def main():
    try:
        ikaslea1 = ikaslea("Ane", 7.5)
        ikaslea1.ikasleaimprimitu()
        ikaslea1.emaitza()

        ikaslea2 = ikaslea("Jon", 3.2)
        ikaslea2.ikasleaimprimitu()
        ikaslea2.emaitza()

        ikaslea3 = ikaslea("Mikel", 12)  
        ikaslea3.ikasleaimprimitu()
        ikaslea3.emaitza()
    
    except ValueError as ve:
        print(f"Salbuespena detektatua: {ve}")  
    
    
    

if __name__ == "__main__":
    main()