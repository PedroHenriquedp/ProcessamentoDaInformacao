# Faça um programa que leia um número inteiro e execute um comando sobre este.
#
#Não é necessário o uso de funções que operem sobre strings. Aliás, não recomendo usar strings para resolver esta pergunta. Note que a leitura da entrada deve ser apenas UM inteiro.
#Entrada
#
#Faça um programa que leia um número N e uma string C. Se a string C for igual “TROCA” ou “INSERE”, então o seu programa deve ler mais dois inteiros I e D, onde 0 <= D <= 9, nesta respectiva ordem.
#Saída
#
#O seu programa deve imprimir o número M obtido de acordo com as seguintes regras.
#
#    Se C é igual à “TROCA”, então M é o número obtido pela troca do I-ésimo dígito, da direita para à esquerda, de N pelo dígito D.
#
#   Se C é igual à “APAGA”, então M é o número obtido pela remoção do I-ésimo dígito, da direita para à esquerda, de N.
#
#    Se C é igual à “INSERE”, então M é o número obtido pela inserção do dígito D à esquerda do I-ésimo dígito, da direita para à esquerda, de N.

def manipulando():

    inteiro = input()
    string = input().upper()
    inteiros = []
    um = 1

    if string == "TROCA" or string == "INSERE":
        D = int(input())
        I = int(input())



    if string == "INSERE":
        for i in range(0, len(inteiro), um):
            inteiros.append((inteiro[i:i + um]))

        inteiros.insert(len(inteiros)+1-D, I)

        print(inteiros)



resultado = manipulando()