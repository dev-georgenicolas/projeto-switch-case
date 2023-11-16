x = int(input("Escolha qual programa você deseja executar:\n[1]Raiz Quadrada\n[2]Cédulas\n[3]Relógio Digital\n[4]Programa 4\n"))

match x:
    case 1:
        n = int(input("Digite um número para saber sua raiz quadrada:"))
        b = 2
        pSquare = 0
        while True:
            if (n-pSquare)< 0.0001 and (n-pSquare)>=0:
                    break
            else:
                p = (b+(n/b))/2
                b = p
                pSquare = p**2
    case 2:
        valor = float(input("Digite o valor a pagar: "))
        cedulas = 0
        atual = 100
        apagar = valor

        while True:
            if atual <= apagar:
                apagar -= atual
                cedulas += 1
            else:
                if cedulas > 0 and atual >= 1:
                    print(f"{cedulas} cédula(s) de R${atual:.2f}")
                elif cedulas > 0:
                    print(f"{cedulas} moeda(s) de R${atual:.2f}")
                if apagar == 0:
                    break
                if atual == 100:
                    atual = 50
                elif atual == 50:
                    atual = 20
                elif atual == 20:
                    atual = 10
                elif atual == 10:
                    atual = 5
                elif atual == 5:
                    atual = 2
                elif atual == 2:
                    atual = 1
                elif atual == 1:
                    atual = 0.5
                elif atual == 0.5:
                    atual = 0.25
                elif atual == 0.25:
                    atual = 0.1
                    atual = 0.05
                elif atual == 0.05:
                    atual = 0.02
                elif atual == 0.02:
                    atual = 0.01
                elif atual == 0.01:
                    atual = 0.005
                elif atual == 0.005:
                    atual = 0.002
                elif atual == 0.002:
                    atual = 0.001

                cedulas = 0
    case 3:
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