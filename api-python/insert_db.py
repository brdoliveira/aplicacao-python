import mysql.connector
from credentials import usr, pswd

mydb = mysql.connector.connect(
    host="localhost",
    user=usr,
    password=pswd,
    database="banco_filmes"
)


def insert_db(titulo,lancamento,duracao,genero,diretor,linguagem) -> None:
    mydb.connect()
    try:

        if mydb.is_connected():
            # db_info = mydb.get_server_info()
            # print("Conectado ao MySQL Server versão ", db_info)

            mycursor = mydb.cursor()

            sql_query = "INSERT INTO banco_filmes.dados(idFilme,titulo,lancamento,duracao,genero,diretor,linguagem) VALUES (null,%s,%s,%s,%s,%s,%s)"

            val = (titulo,lancamento,duracao,genero,diretor,linguagem)

            mycursor.execute(sql_query, val)

            mydb.commit()

            # print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL: ", e)
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            # print("Conexão com MySQL está fechada\n")

