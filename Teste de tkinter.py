
from tkinter import *


root = Tk()
root.title("Cadastro de Cliente")
root.geometry("400x700")
root.configure(bg='lightblue')

# Rótulo para a primeira caixa de entrada Nome
label1 = Label(root, text="Nome: " )
label1.grid(row=0, column=0, padx=10, pady=10)            ## Localização das caixas de texto

# Caixa de entrada de texto para o Nome
entrada_nome = Entry(root,)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)    ## Localização das caixas de texto

## Rótulo para a segunda caixa de entrada Endereço
label2 = Label(root, text="Endereço: ")
label2.grid(row=2, column=0, padx=10, pady=10)            ## Localização das caixas de texto

## Caixa para entranda de texto Endereço
entrada_endereco = Entry(root,)
entrada_endereco.grid(row=2, column=1, padx=10, pady=10)  ## Localização das caixas de texto

## Rótulo para a terceira caixa de entrada telefone
label3 = Label(root, text="Telefone: ")
label3.grid(row=3, column=0, padx=10, pady=10)            ## Localização das caixas de texto

## Caixa de entrada de texto Telefone
entrada_telefone = Entry(root,)
entrada_telefone.grid(row=3, column=1, padx=10, pady=10)  ## Localização das caixas de texto

## Rótulo para a terceira caixa de entrada email
label4 = Label(root, text="Email: ")
label4.grid(row=4, column=0, padx=10, pady=10)            ## Localização das caixas de texto

## Caixa de entrada de texto Email
entrada_email = Entry(root,)
entrada_email.grid(row=4, column=1, padx=10, pady=10)     ## Localização das caixas de texto

 
                      ##################  Campo de Botão  ###################

# Botão para obter texto Confirmação
botao = Button(root,text="Confirmação")
botao.place(x=300, y=10)           ## Localização das caixas de texto

resultado_label = Label(root, text="")
resultado_label.place(x=20 , y=170)


root.mainloop()

