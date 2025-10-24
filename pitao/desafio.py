import random

tabuleiro = [["~" for _ in range(5)] for _ in range(5)]


tesouro_linha = random.randint(0, 4)
tesouro_coluna = random.randint(0, 4)


tentativas = 7

print("=== 🏴‍☠️ JOGO CAÇA AO TESOURO 🏴‍☠️ ===")
print("Tente encontrar o tesouro escondido no tabuleiro 5x5!")
print("Você tem 7 tentativas.\n")


def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))
    print()


for tentativa in range(1, tentativas + 1):
    print(f"Tentativa {tentativa} de {tentativas}")
    mostrar_tabuleiro()


    try:
        linha = int(input("Digite a linha (0 a 4): "))
        coluna = int(input("Digite a coluna (0 a 4): "))
    except ValueError:
        print(" Entrada inválida! Digite números inteiros.\n")
        continue

 
    if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
        print(" Posição fora do tabuleiro! Tente novamente.\n")
        continue

    if tabuleiro[linha][coluna] in ["X", "T"]:
        print(" Você já tentou essa posição! Escolha outra.\n")
        continue

    if linha == tesouro_linha and coluna == tesouro_coluna:
        tabuleiro[linha][coluna] = "T"
        mostrar_tabuleiro()
        print(" Parabéns! Você encontrou o tesouro! ")
        break
    else:
        tabuleiro[linha][coluna] = "X"
       
        dica = []
        if linha < tesouro_linha:
            dica.append("mais para BAIXO")
        elif linha > tesouro_linha:
            dica.append("mais para CIMA")
        if coluna < tesouro_coluna:
            dica.append("mais para a DIREITA")
        elif coluna > tesouro_coluna:
            dica.append("mais para a ESQUERDA")

        print(" Tesouro não está aqui.")
        print(" Dica:", " e ".join(dica), "\n")

else:

    print(" Suas tentativas acabaram!")
    print(f"O tesouro estava na posição ({tesouro_linha}, {tesouro_coluna}).")

mostrar_tabuleiro()
print("=== Fim do jogo! ===")
