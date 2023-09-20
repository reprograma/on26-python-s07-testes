def calcular_media(numeros):
    if not numeros:
        return 0
    elif len(numeros) !=0:
        media= round(sum(numeros) / len(numeros), 2)
        return media