import time
time.sleep(0.2)

print("Brasil x Argentina")
print("Neymar está escalado no time")

camisa = int(input("Qual camisa Neymar irá usar? "))

if camisa == 11:
    print("Neymar fica feliz por você ter dado a camisa 11 a ele!!!")
    
else:
    print("Neymar aceita a camisa apesar de estar esperando outra")
    

print("Começa o jogo")

tempo = 0
gol_do_neymar = False  

while tempo <= 90:
    print("Minutos:", tempo)
    

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
            messi = input("Messi começa a fazer você dançar, e você tem 3 opções. [Arranca as pernas dele] [dar o bote] [pedir por misericórdia]")
            

    tempo += 1

if tempo > 90:
    print("Fim de jogo!")
    

    if gol_do_neymar:
        print("Vitória do Brasil com golaço do Neymito")
        
    else:
        print("O jogo terminou em vitória da Argentina")
        