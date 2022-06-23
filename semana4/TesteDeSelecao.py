#Faça um programa que leia 4 números inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem “Valores aceitos”, senão escrever “Valores nao aceitos”.

#Entrada:
#
#A entrada contém quatro números inteiros.
#Saída:
#
#Seu programa deve imprimir na tela a mensagem “Valores aceitos” ou “Valores nao aceitos”.
#OBS. A impressão na tela não deve conter palavras com acentuação.
numeros =[]
for i in range(0,4):
    numeros.append(int(input()))

if numeros[1] > numeros[2] and numeros[3] > numeros[0] and numeros[2]+numeros[3] > numeros[0]+numeros[1] and numeros[2] >= 0 and numeros[3] >=0 and numeros[0]%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")