from tkinter import *
import conexao_cliente # Meu primeiro módulo para deixar o codigo do app mais limpo e facil

########## ###  Esse import conexao_cliente tem um programa de inserção  de dados com a linguagem MYSQL em uma tabela cliente.



root = Tk()                                                   ##  O import que faz você ver a magica em algo grafico
root.title("Cadastro de Cliente")
root.geometry("400x700")
root.configure(bg='lightblue')

def botao_confirma():                                         ##  A parte do Botão aonde você faz a confirmação de entrada no sql
    nome = entrada_nome.get()
    endereco = entrada_endereco.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()

    conexao_cliente.Cliente(nome, endereco, telefone, email)            # Chama a função Cliente do modulo (conexao_cliente).
    resultado_label.config(text="Cliente inserido com sucesso!")


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

botao = Button(root, text="Confirmação", command=botao_confirma)
botao.place(x=300, y=10) 

resultado_label = Label(root, text="")
resultado_label.place(x=20 , y=170)

root.mainloop()

