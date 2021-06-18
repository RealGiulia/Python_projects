import random

def jogar():
    print("****************************************")
    print("Seja bem-vindo ao jogo de Forca!")
    print("****************************************")

    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()


    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0
    tentativa = len(palavra_secreta) + 2
    # Essa lógica pode prejudicar o jogador, pois se ele erra 1 vez,
    # pode perder o jogo se as letras forem diferentes. Logo,seria interessante deixar 2 tentativas a mais, somando-a,
    # ficando como: tentativa = len(palavra_secreta) + 2.

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
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Ainda restam {} tentativas".format(total_tentativa))
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("fim de jogo!")


if __name__ == "__main__":
    jogar()

