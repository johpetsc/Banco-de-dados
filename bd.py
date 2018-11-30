import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='palavra',
    db='trabalhobd',
)
 
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
            print("Task added successfully")
        except:
            print("Oops! Something wrong")
    connection.commit()
finally:
    connection.close()