#Possibilidades de Cenários para testar ao calcular uma média

def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

