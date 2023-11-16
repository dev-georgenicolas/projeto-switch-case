# from time import *
# from tkinter import *

# tela = Tk()  # Cria uma janela
# tela.title('Relógio Digital')  # Titulo da janela
# tela.geometry("600x100") # Tamanho da janela
# horario = Label(tela, font=("Arial", 48)) # Exibe um texto na tela
# horario.pack(anchor="s") # Define a posição do texto

# def relogio(): # Define a função 'relogio'
#     hora = strftime('%H:%M:%S') # Formata o horario atual e transforma em string 
#     horario.config(text=hora) # Define que o texto exibido é a variável 'hora'
#     horario.after(1000, relogio) # Atualiza o texto exibido em horario a cada 1s
# relogio() # Executa a função

# tela.mainloop()  # Mantém a janela aberta


import customtkinter

janela = customtkinter.CTk()
janela.geometry("300x200")
janela.mainloop()
