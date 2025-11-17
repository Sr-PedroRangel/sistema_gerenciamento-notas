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

while True:
    op = input("Deseja inserir um nota? (Para encerrar, digite 'sair)' ").lower().strip()
    if op == "sair":
        break

    nome = input("Digite o nome do aluno:").strip()
    nota1 = float(input("Digite a 1° nota do aluno:").replace(",","."))
    nota2 = float(input("Digite a 2° nota do aluno:").replace(",","."))
    nota3 = float(input("Digite a 3° nota do aluno:").replace(",","."))

    media = (nota1+nota2+nota3) / 3

    if media >= 7:
        print("Aprovado\n")
    elif 5 <= media <= 6.9:
        print("Recuperação\n")
    else:
        print("Reprovado\n")
