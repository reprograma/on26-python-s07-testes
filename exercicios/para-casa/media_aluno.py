def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def calcular_media_aluno():
    notas_aluno = [8.5, 9.0, 7.5, 6.0, 9.5]
    media = calcular_media(notas_aluno)
    print(f"A média do aluno é: {media:.2f}")

if __name__ == "__main__":
    calcular_media_aluno()