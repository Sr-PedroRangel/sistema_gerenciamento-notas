''' Objetivo

Construir um pequeno programa que simule o cálculo da média de um aluno, evoluindo a cada versão.
A proposta permite exercitar entrada de dados, estruturas condicionais, laços, funções e modularização.

🪜 Etapa 1 — Versão Base (sem funções)
Crie um programa que:

Peça o nome do aluno.

Peça três notas (permitir números decimais).

Calcule a média aritmética simples.

Mostre a média e uma mensagem:

Média ≥ 7 → “Aprovado”

Média entre 5 e 6.9 → “Recuperação”

Média < 5 → “Reprovado”

Permita repetir o processo para vários alunos até que o usuário decida sair.

Dica: Use while True, break e condicionais if/elif/else'''


''' Etapa 2 — Versão com Funções
Reescreva o programa criando funções específicas, por exemplo:

ler_notas() → solicita e retorna as três notas.

calcular_media(notas) → recebe uma lista de notas e retorna a média.

verificar_situacao(media) → retorna a situação (“Aprovado”, “Recuperação”, “Reprovado”).

mostrar_resultado(nome, media, situacao) → exibe as informações formatadas.

Objetivo: perceber a clareza e a reutilização do código'''

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



while True:
    op = input("Deseja inserir um aluno? (Para encerrar, digite 'sair'): ").lower().strip()
    if op == "sair":
        break

    nome, lista = ler_notas()
    media = calcular_media(lista)
    situacao = verificar_situacao(media)
    mostrar_resultado(nome, media, situacao)
