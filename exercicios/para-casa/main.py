from media import media_2


try:
    print(media_2('15',15))
except AssertionError as e:
    print(f"Resultado inválido: \n {e}")

print(f"\n O resultado da média entre 10 e 6.5 é: {media_2(10, 6.5)}")

