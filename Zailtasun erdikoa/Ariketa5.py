def amaiera_amankomuna(str1,str2):
    
    hitza1 = len(str1)
    hitza2 = len(str2)
    max = 0
    for i in range(1, min(hitza1, hitza2) + 1):
        if str1[-i:] == str2[-i:]:
            max = i
            
    return str1[-max:]
        
        
    


izena1 = input("Sartu hitza: ")
izena2 = input("Sartu bigarren hitza: ")

print("Amankomunean dutena: ",amaiera_amankomuna(izena1,izena2))

