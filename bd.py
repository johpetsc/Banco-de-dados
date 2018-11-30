import pymysql
 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='palavra',
    db='trabalhobd',
)

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
                print("Task added successfully")
            except:
                print("Oops! Something wrong")
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
                print("Oops! Something wrong")
        connection.commit()
    finally:
        connection.close()

def update():
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE pessoa SET p_nome=%s, u_nome=%s WHERE cpf = %s"
            try:
                cursor.execute(sql, ('Joao', 'Doido', 1))
                print("Successfully Updated...")
            except:
                print("Oops! Something wrong")
    
        connection.commit()
    finally:
        connection.close()

def delete():
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM pessoa WHERE cpf = %s"
            try:
                cursor.execute(sql, (1))
                print("Successfully Deleted...")
            except:
                print("Oops! Something wrong")
    
        connection.commit()
    finally:
        connection.close()


#create()
read()
#update()
#delete()
