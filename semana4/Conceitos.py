# Após o período de Recuperação, a Universidade Federal do ABC adota por padrão o seguinte critério para Aprovação, Reprovação por desempenho ou Reprovação por frequência:
#
#    Conceitos Finais A, B, C ou D → APROVADO
#
#    Conceitos Finais D ou F → REPROVADO POR DESEMPENHO
#
#    Conceito Final O → REPROVADO POR FREQUENCIA
#
#Faça um programa que recebe como entrada o Conceito Final e imprima a mensagem correspondente. Valide a entrada de forma que o programa emita um aviso ao usuário caso o Conceito Final não seja A, B, C, D, F ou O
#
#Entrada
#
#    A entrada contém um caractere maiúsculo representando o Conceito Final.
#
#Saída
#
#Seu programa deve imprimir na tela a mensagem correspondente (APROVADO, REPROVADO POR DESEMPENHO ou REPROVADO POR FREQUENCIA) ou a mensagem “Conceito invalido!”, caso o Conceito Final não seja A, B, C, D, F ou O. ATENÇÃO: A saída não contém acentuação!

def conceitosFinais():
    nota = input().upper()

    if nota == "A":
        print(f"APROVADO")
    elif nota == "B":
        print(f"APROVADO")
    elif nota == "C":
        print(f"APROVADO")
    elif nota == "D":
        print(f"APROVADO")
    elif nota == "F":
        print(f"REPROVADO POR DESEMPENHO")
    elif nota == "O":
        print(f"REPROVADO POR FREQUENCIA")
    else:
        print(f"Conceito invalido!")

resultado = conceitosFinais()