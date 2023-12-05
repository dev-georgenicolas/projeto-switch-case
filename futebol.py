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

while tempo <= 90:
    print("Minutos:", tempo)
    time.sleep(0.2)

    if tempo == 34:
        jogador = input("Quem marcou o gol? ")

        if jogador.lower() == "neymar":
            gol_do_neymar = True
            print("GOOOOOL! ENCARA NEYMAR MANITOO. Neymar faz um golaço driblando esses bagres e mete a bola pra dentro.")
            
        else:
            print("Olhamos no VAR, e na verdade quem marcou o gol foi", jogador)
            

    else:
        print("Nada de especial aconteceu neste minuto.")
        
        if tempo == 51:
            messi = int(input("Messi começa a fazer você dançar, e você tem 3 opções. [1 - Arranca as pernas dele] [2 - dar o bote] [3 - pedir por misericórdia]"))
            match messi:
                case 1:
                    print("você derruba ele e o lesiona")
                    juiz = int(input("Você lesiona messi, e o juiz mostrou o cartão vermelho pra você, o que você faz? [1 - Você peita o juiz, afirmando ter sido so na bola, e começa a discutir] [2 - Você mantem a calma e pede educadamente para o juiz olhar o VAR]"))
                    match juiz:
                        case 1:
                            print("Você é expulso por reclamação")
                            juiz2 = False
                            break
                        case 2:
                            print("O juiz olha no var e realmente vê que foi so na bola, e anula sua expulsão")
                            juiz2 = True
                case 2:
                    print("você tenta tomar a bola dele dando um bote, mas ele corta pra direita, te deixando no chão e depois ele chuta de fora da area, botando a bola la onde a coruja dorme")
                case 3:
                    print("Você pede por misericordia, porem o messi por ser argentino, e ter maldade no coração, aproveita o momento de sua distração, e mete a bola por debaixo de suas pernas, e sai driblando todo mundo, metendo um golaço por cima do goleiro")
                case _:
                    print("Escolha de um a 3 mano")
                    break


    tempo += 1

if tempo > 90:
    print("Fim de jogo!")
    

    if gol_do_neymar:
        print("Vitória do Brasil com golaço do Neymito")
    elif messi:
        print("Argentina 1 X Brasil 1, o jogo vai pra prorrogação")
        if juiz2:
            print("Começa o jogo")
