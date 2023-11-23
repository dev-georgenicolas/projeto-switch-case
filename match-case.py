x = int(input("Escolha qual programa você deseja executar:\n[1]Raiz Quadrada\n[2]Cédulas\n[3]Relógio Digital\n[4]Programa 4\n"))

match x:
    case 1:
        
    case 2:

    case 3:
        from time import *
        from tkinter import *

        tela = Tk()
        tela.title('Relógio Digital')
        tela.geometry('400x100')

        horario = Label(tela, font=('Arial', 48))
        horario.pack(anchor='s')

        def relogio():
            hora = strftime('%H:%M:%S')
            horario.config(text=hora)
            horario.after(1000, relogio)
        relogio()

        tela.mainloop()
