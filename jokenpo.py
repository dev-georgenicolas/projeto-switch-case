import random
import time

ptspc = 0
ptsuser = 0 

while True:
    y = int(input("[1]Pedra\n[2]Papel\n[3]Tesoura\n"))
    time.sleep(0.3)

    x = [1, 2, 3]
    z = random.choice(x)

    if z == 1:
        print("Oponente escolheu Pedra")
    elif z == 2:
        print("Oponente escolheu Papel")
    else:
        print("Oponente escolheu Tesoura")



    if y == z:
        print("Empate!")
    elif (y == 1 and z == 3) or (y == 2 and z == 1) or (y == 3 and z == 2):
        ptsuser +=1
        print(f"Seus pontos: {ptsuser}\nPontos do oponente: {ptspc}")
    else:
        ptspc +=1
        print(f"Seus pontos: {ptsuser}\nPontos do oponente: {ptspc}")

    if ptsuser == 2:
        print("Você ganhou!!!")
        break

    if  ptspc == 2:
        print("Você perdeu!")
        break