# Calculando a média de uma lista de números

def calcular_media(numeros):               # definindo a função para cálculo da média
    if not numeros:                        # se não tiver números, retorne 0
        return None
    return sum(numeros) / len(numeros)     # se tiver números, some os números e divida pelo tamamho do vetor de números

