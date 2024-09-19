def gehiketa(a , b):
    try:
        return a + b
    except TypeError:
        print("Akatsa: datu mota baliogabea.")

def kenketa(a , b):
    try:
       return a - b
    except TypeError:
        print("Akatsa: datu mota baliogabea.")

def biderketa(a , b):
    try:
      return  a * b
    except TypeError:
        print("Akatsa: datu mota baliogabea.")


def zatiketa(a , b):
    
    try:
       return a / b
    except TypeError:
        print("Akatsa: datu mota baliogabea.")
    except ZeroDivisionError:
        print("Akatsa: Zenbakia ezin da zeroz zatitu")

    
    
    
