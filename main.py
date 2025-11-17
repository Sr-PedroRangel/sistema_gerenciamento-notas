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

from funcoes import ler_notas, calcular_media, verificar_situacao, mostrar_resultado


resultados = []   # EXTRA 1

while True:
    op = input("Deseja inserir um aluno? (Para encerrar, digite 'sair'): ").lower().strip()
    if op == "sair":
        break

    nome, lista = ler_notas()
    media = calcular_media(lista)
    situacao = verificar_situacao(media)
    mostrar_resultado(nome, media, situacao)


    resultados.append((nome, media, situacao))



print("\n===== RESUMO GERAL DOS ALUNOS CADASTRADOS =====\n")

if len(resultados) == 0:
    print("Nenhum aluno foi registrado.")
else:
    for nome, media, situacao in resultados:
        print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")


