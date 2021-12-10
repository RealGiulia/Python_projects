import random


def jogar():

    msg_abertura()
    palavra_secreta = load_palavra_secreta()

    letras_acertadas = inicia_letra_acertada(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    tentativa = len(palavra_secreta)
   

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
            else:
                erros += 1
        tentativa = tentativa - 1
        total_tentativa = tentativa
        enforcou = (erros == total_tentativa)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Ainda restam {} tentativas".format(total_tentativa))
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("fim de jogo!")


def msg_abertura():
    print("****************************************")
    print("Seja bem-vindo ao jogo de Forca - Frutas!")
    print("****************************************")


def load_palavra_secreta():
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicia_letra_acertada(palavra):
    return ["_" for letra in palavra]


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


if __name__ == "__main__":
    jogar()
