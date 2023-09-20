def calcular_media(numeros):
    if not numeros:
      return 0
    return sum(numeros)/ len(numeros)

numeros = []

numero_de_notas = int(input('Digite o numeros de notas: '))

for i in range(numero_de_notas):
  numero = int(input('Digite uma nota: '))
  numeros.append(numero)

media = calcular_media(numeros)

print(f'A média dos números é: {media:.2f}')