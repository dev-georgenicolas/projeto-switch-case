from tkinter import *
from tkinter import messagebox

jane = Tk()
jane.title("Login")
jane.geometry("340x340")
jane.configure(bg="#333333")

def login():
    user = "nepomuceno"
    senha_user = "123456"
    if nome.get()== user and senha.get() == senha_user:
       messagebox.showinfo(title="Login", message="Você foi logado com sucesso")
    else:
        messagebox.showerror(title="Login", message="Falha ao realizar o login. Usuário ou senha incorretos!")



frame = Frame(bg="#333333")



texto = Label(frame,text="Login", bg="#333333", fg="#FF3399", font=("Arial", 30) )
texto2 = Label(frame,text="Nome", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
nome = Entry(frame, font=("Arial", 16))
senha = Entry(frame, show="*", font=("Arial", 16))
texto_senha = Label(frame, text="Senha", bg="#333333", fg="#FFFFFF", font=("Arial", 16))
login = Button(frame, text="Login", bg="#FF3399", fg="#ffffff", font=("Arial", 16), command=login)

texto.grid(row=0, column=0, columnspan=2, pady=40)
texto2.grid(row=1, column=0)
nome.grid(row=1, column=1,pady=20)
senha.grid(row=2, column=1, pady=20)
texto_senha.grid(row=2, column=0)
login.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

jane.mainloop()


