# Define uma função chamada calculaMedia que calcula a média dos números em uma lista.
def calculaMedia(lista):
    # Verifica se a lista está vazia.
    if not lista:
        return 0  # Se a lista estiver vazia, retorna 0 para evitar divisão por zero.

    # Calcula a soma de todos os elementos na lista usando a função sum.
    soma = sum(lista)

    # Calcula a média dividindo a soma pelo número de elementos na lista.
    media = soma / len(lista)

    # Retorna o resultado da média.
    return media
