"""
Cenários de testes-
1- lista só com números negativos.
2- lista só com zeros.
3- lista vazia
4- se a lista só tiver 1 elemento.
5- se a lista tiver números misturados, positivos e negativos.
"""

def calcular_media(numeros):
    if not numeros:
        return 0
    
    return sum(numeros) / len(numeros)
