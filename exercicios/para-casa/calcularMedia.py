#media = soma de todos os numeros/numero de elementos no conjunto

def calcularMedia(numeros):
    if not numeros:
        return 0
    return sum(numeros)/len(numeros)