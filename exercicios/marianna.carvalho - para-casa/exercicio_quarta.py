# Média = soma de todos os números / número de elementos no conjunto



def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

