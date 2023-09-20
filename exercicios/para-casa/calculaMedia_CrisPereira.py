# Exercício para casa semana 07 - prof Jéssica Lima
# Estudante Cris Pereira

import statistics

def calcular_media (notas=None):
    if not notas:
        return 0
    else:
        return sum(notas)/len(notas)

# notas = []
# media = calcular_media(notas)
# print(f"A média dos valores é: {media:.2f}")