"""
pensar em tudo que pode ser testado que poderia dar errado com media aritmetica:
numeros positivos e negativos
o numero nao existir
o numero a ser dividido estar errado
"""

def calcular_media(numeros):
    if not numeros:
        return 0
    
    return sum(numeros) / len(numeros)