def calcular_media(testes):
    soma = 0
    for teste in testes:
        soma += teste.countTestCases()

    media = soma / len(testes)
    return media