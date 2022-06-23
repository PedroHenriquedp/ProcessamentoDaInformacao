# O Sistema ABO foi o primeiro dos grupos sanguíneos descobertos no início do século XX em 1900, pelo cientista austríaco Karl Landsteiner. Fazendo reagir amostras de sangue de diversas pessoas, ele isolou os glóbulos vermelhos e fez diferentes combinações com o plasma, tendo como resultado a presença de aglutinação dos glóbulos em alguns casos, e sua ausência em outros. Assim, Landsteiner classificou os seres humanos em três grupos sanguíneos: A, B e O, e explicou por que algumas pessoas morriam depois de transfusões de sangue. Mais tarde, em 1902, seus colaboradores von Decastello e Sturli encontraram o grupo AB. Em1930 Landsteiner ganhou o Prêmio Nobel por este trabalho.
#
# O sistema ABO se caracteriza pela presença ou ausência de dois antígenos A e B estabelecendo assim as seguinte regras de compatibilidade entre grupos:

# Indivíduos do grupo O (doador universal) não possuem nenhum dos dois antígenos, portanto possuem anticorpos anti-A e anti-B; podem receber apenas sangue do grupo O, mas podem doar para todos os grupos.

# Indivíduos do grupo A possuem apenas o antígeno A, e portanto apresentam os anticorpos anti-B; podem receber sangue dos grupos O e A, e doar para os grupos A e AB.

# ndivíduos do grupo B possuem apenas o antígeno B, e portanto apresentam os anticorpos anti-A; podem receber sangue dos grupos O e B, e doar para os grupos B e AB.

# Indivíduos do grupo AB (receptor universal) possuem ambos os antígenos, e nenhum anticorpo. Podem receber sangue de qualquer grupo, mas doam apenas para o grupo AB.

# Escreva um programa que receba o grupo sanguíneo de um paciente e de um doador e exiba uma mensagem indicando se estes são compatíveis ou incompatíveis de acordo com o sistema ABO.
# Entrada
#
# A entrada está composta por duas cadeia de caracteres, a primeira cadeia de caracteres corresponde ao tipo sanguíneo do paciente e a segunda cadeia de caracteres corresponde ao tipo sanguíneo do doador. Os valores de entrada são uma das seguintes cadeias: “A”, “B”, “O” e “AB”.
# Saída
#
# Seu programa deve imprimir a frase “transfusao compativel”, caso o grupo sanguíneo do doador seja compativel com o grupo sanguíneo do paciente, ou “transfusao incompativel” caso contrário.

def transfusao():
    paciente = []
    for i in range(0, 2):
        paciente.append(input().upper())
    teste = paciente[0] + paciente[1]
    if teste == "AB" or teste == "BA" or teste == "BAB" or teste == "AAB" or teste == "OAB" or teste == "OB" or teste == "OA":
        verificacao = False
    else:
        verificacao = True

    if verificacao == False:
        print(f"transfusao incompativel")
    else:
        print(f"transfusao compativel")

resultado = transfusao()
