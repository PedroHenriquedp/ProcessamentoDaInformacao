#Faça um programa que leia dois números reais (x e y) que devem representar as coordenadas de um ponto em um plano.
# A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

def coordenada():
    x = float(input())
    y = float(input())
    if x==0 and y!=0:
        print(f"Eixo Y")
    elif y==0 and x!=0:
        print(f"Eixo X")
    elif x==0 and y==0:
        print(f"Origem")
    elif x > 0 and y > 0:
        print(f"Q1")
    elif x < 0 and y > 0:
        print(f"Q2")
    elif x > 0 and y < 0:
        print(f"Q4")
    elif x < 0 and y < 0:
        print(f"Q3")

resultado = coordenada()