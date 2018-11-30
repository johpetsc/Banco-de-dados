import pymysql
import os

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='palavra',
    db='trabalhobd',
)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def create():
    cpf = input("cpf: ")
    p_nome = input("Nome: ")
    u_nome = input("Sobrenome: ")
    data_nascimento = input("Data: ")
    idade = input("Idade: ")
    endereco = input("Endereco: ")

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO pessoa (cpf, p_nome, u_nome, data_nascimento, idade, endereco) VALUES (%s, %s, %s, %s, %s, %s);"
            try:
                cursor.execute(sql, (cpf, p_nome, u_nome, data_nascimento, idade, endereco))
                print("Pessoa adicionada com sucesso.")
            except:
                print("Falha ao adicionar pessoa.")
        connection.commit()
    finally:
        connection.close()

def read():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM pessoa"
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
    
                print("Cpf\tNome\tSobrenome\tData\tIdade\tEndereco")
                print("---------------------------------------------------------------------------")
                for row in result:
                    print(row)
            except:
                print("Falha ao ler tabela.")
        connection.commit()
    finally:
        connection.close()

def update():
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE pessoa SET p_nome=%s, u_nome=%s WHERE cpf = %s"
            try:
                cursor.execute(sql, ('Joao', 'Doido', 1))
                print("Pessoa atualizada com sucesso.")
            except:
                print("Falha ao atualizar pessoa.")
    
        connection.commit()
    finally:
        connection.close()

def delete():
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM pessoa WHERE cpf = %s"
            try:
                cursor.execute(sql, (1))
                print("Pessoa deletada com sucesso.")
            except:
                print("Falha ao deletar pessoa.")
    
        connection.commit()
    finally:
        connection.close()

cls()

print("\t\t\tCRUD para o banco de dados.\n\n")
print("\tCREATE - 1 \n\n\tREAD - 2 \n\n\tUPDATE - 3 \n\n\tDELETE - 4 \n\n\tSair - 0")
opc = input("\n\n\tOpção:")

cls()

if opc == "1":
    create()
elif opc == "2":
    read()
elif opc == "3":
    update()
elif opc == "4":
    delete()
