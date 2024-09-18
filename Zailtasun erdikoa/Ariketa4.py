def positiboak_ordenatu(zenbakiak):
    positiboak = []
    for zen in zenbakiak:
        if zen > 0:
            positiboak.append(zen)
            
    positiboak = sorted(positiboak)
    emaitza = []
    for zen in zenbakiak:
        if zen > 0:
            emaitza.append(positiboak.pop(0))
        else:
            emaitza.append(zen)
    return emaitza

zenbakiak = [6, 3, -2, 5, -8, 2, -2]

print(positiboak_ordenatu(zenbakiak))

