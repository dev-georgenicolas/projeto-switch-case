from time import *
from tkinter import *

tela = Tk()
tela.title('Relógio Digital')
tela.geometry('400x100')
tela.resizable(0, 0)


horario = Label(tela, font=('Arial', 48))
horario.pack(anchor='s')

def relogio():
    hora = strftime('%H:%M:%S')
    horario.config(text=hora)
    horario.after(1000, relogio)
relogio()

tela.mainloop()
