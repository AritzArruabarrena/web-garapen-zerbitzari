def hiriak_ordenatzen(hiriak):
    return sorted([hiri for hiri, populazioa in hiriak.items() if populazioa > 200000], key=lambda h: hiriak[h], reverse=True)
    
    


hiriak = {
    "Bilbo" : 345000,
    "Donostia" : 186000,
    "Gasteiz" : 249000,
    "Madrid" : 3223000,
    "Sevilla" : 688000,
    "Granada" : 232000 
}


print(hiriak_ordenatzen(hiriak))