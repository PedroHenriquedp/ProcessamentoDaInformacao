#Faça um programa que leia três números inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente.
#Entrada
#
#A entrada contém três números inteiros.
#Saída

#Seu programa deve imprimir a saída conforme especificado.

def ordenando():
    numeros = []
    p = 0
    for i in range(0,3):
        numeros.append(int(input()))

    numerosOrdenados = sorted(numeros)

    for i in range(0,3):
        print(numerosOrdenados[i])

resultado = ordenando()