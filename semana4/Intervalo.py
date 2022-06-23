
def intervalo():
    numero = float(input())
    if 0 <= numero <= 25:
        print(f"Intervalo [0,25]")
    elif 25 < numero <= 50:
        print(f"Intervalo (25,50]")
    elif 50 < numero <= 75:
        print(f"Intervalo (50,75],")
    elif 75 < numero <= 100:
        print(f"Intervalo (75,100]")
    else:
        print(f"Fora de intervalo")
resultado = intervalo()