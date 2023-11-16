# Importação das Bibliotecas
from time import *
from tkinter import *

# Configuração da Janela
tela = Tk()  # Cria uma janela
tela.title('Relógio Digital')  # Titulo da janela
tela.geometry('400x100') # Tamanho da janela

# Exibição do Relógio
horario = Label(tela, font=('Arial', 48)) # Exibe um texto na tela
horario.pack(anchor='s') # Define a posição do texto

# Configuração do funcionamento do relógio
def relogio(): # Define a função 'relogio'
    hora = strftime('%H:%M:%S') # Formata o horario atual e transforma em string 
    horario.config(text=hora) # Define que o texto exibido é a variável 'hora'
    horario.after(1000, relogio) # Atualiza o texto exibido em horario a cada 1s
relogio() # Executa a função

tela.mainloop()  # Mantém a janela aberta