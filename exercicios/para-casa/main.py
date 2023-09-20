from media import media_2


try:
    print(media_2('15',15))
except AssertionError as e:
    print(f'Resultado inválido: {e}')
