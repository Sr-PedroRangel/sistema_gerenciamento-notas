def ler_notas():
    nome = input("Digite o nome do aluno: ").strip()

    lista = []
    nota1 = float(input("Digite a 1° nota do aluno: ").replace(",", "."))
    lista.append(nota1)

    nota2 = float(input("Digite a 2° nota do aluno: ").replace(",", "."))
    lista.append(nota2)

    nota3 = float(input("Digite a 3° nota do aluno: ").replace(",", "."))
    lista.append(nota3)

    return nome, lista


def calcular_media(notas: list[float]):
    soman = 0
    for n in notas:
        soman += n
    return soman / 3


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media <= 6.9:
        return "Recuperação"
    else:
        return "Reprovado"


def mostrar_resultado(nome, media, situacao):
    print(f"\nA média do aluno {nome} é {media:.2f}, e ele foi {situacao}\n")

