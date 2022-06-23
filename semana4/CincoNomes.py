#Faça um programa que permita receber cinco nomes de pessoas e identificar se todas tem o mesmo nome. O nome de uma pessoa pode ter espaços em branco

#Entrada

#A entrada está composta por 5 nomes (cadeias de texto).
#Saída

#Seu programa deve indicar se todos os nomes são iguais (“Verdadeiro”) ou não (“Falso”).

nomes = []
for i in range (0,5):
    nomes.append(input())

for i in range (0,5):
    if nomes[0] != nomes[i]:
        verificacao = False
        break
    else:
        verificacao = True

if verificacao == True:
    print("Verdadeiro")
else:
    print("Falso")