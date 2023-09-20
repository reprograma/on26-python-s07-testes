def calcular_media(numeros):
    if not numeros:
        return 0
    return round(sum(numeros) / len(numeros), 2)
        

