def calcular_media(valores):
    if not valores:
        return 0
    
    return round(sum(valores)/len(valores),2)