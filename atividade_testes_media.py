## TENTAR QUEBRAR O CÓDIGO DE MÉDIA ARITMÉTICA
## CALCULANDO A MEDIA DE UMA LISTA

def calcular_media(numeros):
    if not numeros:
        return 0
    
    return sum(numeros) / len(numeros)