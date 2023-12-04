import time

print("Brasil x Argentina")
print("Neymar está escalado no time")

camisa = int(input("Qual camisa Neymar irá usar? "))
time.sleep(0.2)

if camisa == 11:
    print("Neymar fica feliz por você ter dado a camisa 11 a ele!!!")
else:
    print("Neymar aceita a camisa apesar de estar esperando outra")

print("Começa o jogo")

tempo = 0
gol_do_neymar = False
messi_gol = False
juiz2 = False

while tempo <= 90:
    print("Minutos:", tempo)
    time.sleep(0.2)

    if tempo == 34:
        jogador = input("Quem marcou o gol? ")

        if jogador.lower() == "neymar":
            gol_do_neymar = True
            print("GOOOOOL! ENCARA NEYMAR MANITOO. Neymar faz um golaço driblando esses bagres e mete a bola pra dentro.")
        else:
            print(f"Olhamos no VAR, e na verdade quem marcou o gol foi {jogador}")

    else:
        print("Nada de especial aconteceu neste minuto.")

        if tempo == 51:
            messi = int(input("Messi começa a fazer você dançar, e você tem 3 opções. [1 - Arranca as pernas dele] [2 - dar o bote] [3 - pedir por misericórdia]"))

            match messi:
                case 1:
                    print("Você derruba ele e o lesiona")
                    juiz = int(input("Você lesiona messi, e o juiz mostrou o cartão vermelho pra você, o que você faz? [1 - Você peita o juiz, afirmando ter sido só na bola, e começa a discutir] [2 - Você mantém a calma e pede educadamente para o juiz olhar o VAR]"))

                    match juiz:
                        case 1:
                            print("Você é expulso por reclamação")
                            juiz2 = False
                        case 2:
                            print("O juiz olha no VAR e realmente vê que foi só na bola, e anula sua expulsão")
                            juiz2 = True
                case 2:
                    print("Você tenta tomar a bola dele dando um bote, mas ele corta para a direita, te deixando no chão e depois ele chuta de fora da área, botando a bola lá onde a coruja dorme")
                    messi_gol = True
                case 3:
                    print("Você pede por misericórdia, porém o Messi, por ser argentino, e ter maldade no coração, aproveita o momento de sua distração, e mete a bola por debaixo de suas pernas, e sai driblando todo mundo, metendo um golaço por cima do goleiro")
                    messi_gol = True
                case _:
                    print("Escolha de um a 3 mano")

    tempo += 1

if tempo > 90:
    print("Fim de jogo")

    if gol_do_neymar:
        print("Vitória do Brasil com golaço do Neymito")
    elif messi_gol:
        print("Argentina 1 X Brasil 1, o jogo vai pra prorrogação")
        if juiz2:
            print("Começa a prorrogação")

            tempo_prorrogacao = 0
            while tempo_prorrogacao <= 30:  
                print("Minutos na prorrogação:", tempo_prorrogacao)
                time.sleep(0.2)
                tempo_prorrogacao += 1

            print("Fim da prorrogação! Brasil X Argentina saiu 0 a 0")
