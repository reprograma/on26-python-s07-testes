# Falar o que pode ser melhorado no código:
# Fazer pelo menos 4 codigos e 4 comentários
# Usar o false ou verdadeiro para determinada valor
# Calacular a média da lista vazia



def calculaMedia(lista):
    if not lista:
        return 0

    return sum(lista) / len(lista)