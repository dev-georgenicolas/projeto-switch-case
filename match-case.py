x = int(input("Escolha uma das opções abaixo:\n[1]Futebol\n[2]Calcular Idade\n[3]Login\n[4]Relógio Digital")

match x:
    case 1:
       import futebol
    case 2:
       import idade
    case 3:
       import login
    case 4:
       import relogio
