def calcular_media(numeros):
    if not numeros:
        return None
    
    return sum(numeros)/len(numeros)


def main():
    numeros = []

    while True:
        try:
            numero = float(input("Digite um número para calcular a média. Se não tiver mais números, digite S\n"))
            numeros.append(numero)
        except(ValueError):
            break
    print(f"A média é: {calcular_media(numeros)}")

if __name__ == "__main__":
    main()