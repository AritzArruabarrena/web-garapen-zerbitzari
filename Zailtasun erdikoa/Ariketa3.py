def gehiengo_absolutua(botoak):
    gehiengo = len(botoak) // 2  
    for voto in set(botoak):  
        if botoak.count(voto) > gehiengo:  
            return voto , "alderdiak gehiengo absolutua lortu du" 
    return "Inork ez dauka gehiengo absoluturik" 

botoak = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'H']

print(gehiengo_absolutua(botoak))
