from media import media


try:
    print(media('10',15))
except AssertionError as e:
    print(f"Resultado inválido: \n {e}")

print(f"\n O resultado da média entre 10 e 15 é: {media(10, 15)}")

