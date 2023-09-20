"""def calcular_media(numeros):
    if not numeros:
        return None 
    return sum (numeros)/ len(numeros)
"""

def calcular_media(numeros):
    numeros_validos = [x for x in numeros if isinstance(x, (int, float))]
    if not numeros_validos:
        return None
    return sum(numeros_validos) / len(numeros_validos)



    
    
    