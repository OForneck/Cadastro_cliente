import pymysql

def Cliente(nome, endereco, telefone, email):
        con = pymysql.connect(db='Seu banco de dados', user='Seu usuario', passwd='Sua senha')        ### Conexão com o bdd

        cursor = con.cursor()

        cursor.execute("INSERT INTO Cliente (nome, endereco, telefone, email) VALUES (%s, %s, %s, %s)", (nome, endereco, telefone, email))


        con.commit()

        con.close()
