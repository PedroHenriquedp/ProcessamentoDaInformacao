#Escreva um programa que leia os comprimentos (números inteiros positivos) dos lados de um triângulo. Após isso, verifique se é um triângulo válido. Observação: para um triângulo ser válido, nenhum dos lados pode ser maior que a soma dos outros dois lados. Adicionalmente, verifique se é um triângulo retângulo.
#
#DICA: para saber se um triângulo é retângulo, encontre o lado maior e veja se ele é igual à soma dos quadrados dos outros dois lados.
#Entrada:
#
#Comprimento de cada um dos três lados (número inteiro positivo)
#
#Saída:
#
#Seu programa deve imprimir "VALIDO" se for um triângulo válido ou "INVALIDO" se não for. Importante: observe que a letra "A" em "VALIDO"/"INVALIDO" não tem acento neste programa. Adicionalmente, imprima "RETANGULO" (sem acento) se for um triângulo retângulo.

def triangulo():
    ladosTriangulo = []


    for i in range(0,3):
        ladosTriangulo.append(int(input()))


    teste1 = abs(ladosTriangulo[1] - ladosTriangulo[2])
    teste2 = abs(ladosTriangulo[0] - ladosTriangulo[2])
    teste3 = abs(ladosTriangulo[1] - ladosTriangulo[0])

    for i in range(len(ladosTriangulo)):
        if ladosTriangulo[i] > 0:
            verificacao = True
        else:
            verificacao = False
            print(f"INVALIDO")
            break

    if verificacao == True:
        if ladosTriangulo[1] + ladosTriangulo[2] > ladosTriangulo[0] > teste1 or ladosTriangulo[0] + ladosTriangulo[2] > ladosTriangulo[1] > teste2 or ladosTriangulo[1] + ladosTriangulo[0] > ladosTriangulo[2] > teste3:
            print(f"VALIDO")
        else:
            print(f"INVALIDO")

        ladosDecrescentes = sorted(ladosTriangulo)
        if ladosDecrescentes[2] ** 2 == (ladosDecrescentes[0] ** 2 + ladosDecrescentes[1] ** 2):
            print(f"RETANGULO")

resultado = triangulo()