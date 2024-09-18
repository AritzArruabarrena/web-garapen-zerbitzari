from jendea import Pertsona


def irakurri():
    hiztegia = []
    with open('Ariketa1/jendea.txt' , 'r') as f:
        content = f.readlines()
        for filak in content:
            id, izena, abizena , jaiotza_data = filak.split(";") 
            pertsona = Pertsona(id,izena,abizena,jaiotza_data)
            hiztegia.append(pertsona)

    return hiztegia


hiztegia = irakurri()

for pertsona in hiztegia:
    print(pertsona)


