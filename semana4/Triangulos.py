#Leia 3 valores reais A, B e C e ordene-os em ordem decrescente, de modo que A >= B >= C. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos:
#Se A >= B+C, apresente a mensagem “NAO FORMA TRIANGULO”
#Se A² = B² + C², apresente a mensagem “TRIANGULO RETANGULO”
#Se A² > B² + C², apresente a mensagem “TRIANGULO OBTUSANGULO”
#Se A² < B² + C², apresente a mensagem “TRIANGULO ACUTANGULO”
#
#Se os três lados forem iguais, apresente a mensagem “TRIANGULO EQUILATERO”
#
#Se apenas dois dos lados forem iguais, apresente a mensagem “TRIANGULO ISOSCELES”
#Entrada
#
#A entrada contém três valores reais positivos A, B e C correspondentes aos três lados de um triângulo.
#Saída
#
#Imprima todas as classificações do triângulo especificado na entrada. Note que um triângulo pode ter mais de uma classificação.

def classificandoTriangulos():
    numeros = []
    for i in range(0,3):
        numeros.append(float(input()))
    numerosOrdenados = sorted(numeros)

    if numerosOrdenados[2] >= numerosOrdenados[1]+numerosOrdenados[0]:
        print(f"NAO FORMA TRIANGULO")
    if numerosOrdenados[2]**2 == numerosOrdenados[1]**2+numerosOrdenados[0]**2:
        print(f"TRIANGULO RETANGULO")
    if numerosOrdenados[2]**2 > numerosOrdenados[1]**2+numerosOrdenados[0]**2:
        print(f"TRIANGULO OBTUSANGULO")
    if numerosOrdenados[2]**2 < numerosOrdenados[1]**2+numerosOrdenados[0]**2:
        print(f"TRIANGULO ACUTANGULO")
    if numerosOrdenados[0] == numerosOrdenados[1] == numerosOrdenados[2]:
        print(f"TRIANGULO EQUILATERO")

    for i in numerosOrdenados:
        if numerosOrdenados.count(i) == 2:
            verificacao = True
            break

    if verificacao == True:
            print(f"TRIANGULO ISOSCELES")

resultado = classificandoTriangulos()