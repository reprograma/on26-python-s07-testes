# notas = [9, 7, 8, 5]
# calculo_soma = sum(notas)
# numero_elementos = len(notas)
# calculo_media = calculo_soma / numero_elementos
#Cenário 1 - Calcular média de valores de uma lista
def calculo_media(numeros):
    if not numeros:
        return 0
    
    return sum(numeros) / len(numeros)