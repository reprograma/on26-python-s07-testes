#definir calculo da média
def media(lista):
    if not lista:
        return 0
    soma = 0
    for numero in lista:
        soma += numero
    return round(soma / len(lista))


#listas de teste
#os cenários pensando foram situações com lista vazia, lista unitária, lista com numeros repetidos, lista com numeros fora do intervalo.
#lista vazia
lista_vazia = []
media_esperadaV= 0
calculo_mediaV= media(lista_vazia)
assert media_esperadaV==calculo_mediaV
print (f'a média é {calculo_mediaV}')

#lista unitária
lista_unitaria=[1]
media_esperada_unitaria=1
calaculo_media_unitaria=media(lista_unitaria)
assert media_esperada_unitaria==calaculo_media_unitaria
print(f'a média é {calaculo_media_unitaria}')

#lista com numeros repitidos
lista_numerosR = [7,7,7,7,7,7,7,7]
media_espera_numerosR=7
calculo_media_repitidos= media(lista_numerosR)
assert media_espera_numerosR==calculo_media_repitidos
print (f'a média é {calculo_media_repitidos}')

#lista com numeros fora do intervalo
lista_num_fora_intervalo=[100, 200]
media_esperada_fi=None
calculo_media_fi=media(lista_num_fora_intervalo)
assert calculo_media_fi==calculo_media_fi
print (f'a média é {calculo_media_fi}')