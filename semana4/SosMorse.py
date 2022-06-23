#Faça um programa que permita identificar se existe algum pedido de ajuda em uma determinada mensagem MORSE.
#Neste exercício, cada mensagem usada na transmissão, inicia e termina com um número inteiro de apenas um digito.
#Cada letra é separada por um espaço em branco. Cada palavra é separada por uma barra.
#Note que um pedido de ajuda (sos) é representado por “... --- ...”

#OBS: Pode testar (e ouvir) com mais entradas usando a seguinte página de codificação de texto: https://morsecode.world/international/translator.html
#
#DICA 1: Lembre-se de que o pedido de ajuda deve conter isoladamente a palavra "sos" em código Morse
#
#DICA 2: Use o comando if "????" in <variável da mensagem>:  do Python para verificar se a sequencia de caracteres ???? está contida na mensagem
#
#
#Entrada
#
#A entrada contém uma mensagem (cadeia de texto) codificada em MORSE.
#Saída
#
#Seu programa deve indicar se a mensagem contem algum pedido de ajuda.

def codigoMorse():
    mensagem = input()
    mensagem = mensagem.split("/")

    print(mensagem)
    for i in range(len(mensagem)):
        if mensagem[i] == "... --- ..." or mensagem[i] == " ... --- ... " or mensagem[i] == " ... --- ..." or mensagem[i] == "... --- ... ":
            verificacao = True
            break
        else:
            verificacao = False

    if verificacao == True:
        print(f"Mensagem com pedido de ajuda!")
    else:
        print(f"Mensagem sem pedido de ajuda!")



resultado = codigoMorse()