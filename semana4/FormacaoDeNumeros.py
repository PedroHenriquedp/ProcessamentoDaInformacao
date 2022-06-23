#Faça um programa que permita receber apenas um número inteiro (de no máximo 3 dígitos) e imprima a sua formação em centenas, dezenas e milhares.
#Entrada
#
#A entrada está composta por apenas um número inteiro maior a zero e menor a 1000.
#Saída
#
#Seu programa deve imprimir a formação do número em ‘centenas’, ‘dezenas’ e ‘unidades’. Veja exemplos de formatação.


def Segregacao():
    numero = int(input())
    centena = numero
    centena = centena // 100
    dezena = (numero - (centena * 100)) // 10
    unidade = (numero - ((centena * 100) + (dezena * 10))) // 1

    if dezena == 0 and unidade == 0:
        print(f"{centena} centenas")
    elif centena == 0 and dezena == 0:
        print(f"{unidade} unidades")
    elif unidade == 0 and centena == 0:
        print(f"{dezena} dezenas")

    elif unidade == 0:
        print(f"{centena} centenas")
        print(f"e")
        print(f"{dezena} dezenas")
    elif dezena == 0:
        print(f"{centena} centenas")
        print(f"e")
        print(f"{unidade} unidades")
    elif centena == 0:
        print(f"{dezena} dezenas")
        print(f"e")
        print(f"{unidade} unidades")
    else:
        print(f"{centena} centenas")
        print(f"e")
        print(f"{dezena} dezenas")
        print(f"e")
        print(f"{unidade} unidades")


resultado = Segregacao()
