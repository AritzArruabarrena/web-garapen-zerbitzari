import datetime

def main():
    x = input("Mesedez sartu zure jaiotze eguna (AAAA-MM-DD): ")
    
    try:
        date_obj = datetime.datetime.strptime(x, "%Y-%m-%d")
        print(f"Zure jaiotze data hau da: {date_obj.strftime('%Y-%m-%d')}")

        asteko_eguna = date_obj.strftime("%A")
        print(f"Zure jaiotze eguna asteko {asteko_eguna} zen.")

        gaurko_eguna = datetime.datetime.now()
        
        urtebetetzea = date_obj.replace(year=gaurko_eguna.year)

        if urtebetetzea < gaurko_eguna:
            urtebetetzea = date_obj.replace(year=gaurko_eguna.year + 1)

        faltadirenegunak = (urtebetetzea - gaurko_eguna).days

        if faltadirenegunak == 0:
            print("Zorionak! Gaur da zure urtebetetzea!")
        else:
            print(f"Zure hurrengo urtebetetzerako {faltadirenegunak} egun falta dira.")

    except ValueError:
        print("Ez duzu formatu egokian sartu (AAAA-MM-DD).")

if __name__ == "__main__":
    main()
