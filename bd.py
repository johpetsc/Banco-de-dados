import pymysql
import os
import sys

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='palavra',
    db='trabalhobd',
)

def stop():
    print("\n\n\n\t\tPressione Enter para continuar.")
    sys.stdin.read(1)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def create():
    tab = input("\n\n\n\tNome da tabela onde será feita a operação INSERT: ")
    cls()

    if tab == "pessoa":
        cpf = input("\tCPF: ")
        nome = input("\tNome: ")
        sobrenome = input("\tSobrenome: ")
        data = input("\tData: ")
        idade = input("\tIdade: ")
        endereco = input("\tEndereço: ")  
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO pessoa (cpf, p_nome, u_nome, data_nascimento, idade, endereco) VALUES (%s, %s, %s, %s, %s, %s);"
                try:
                    cursor.execute(sql, (cpf, nome, nome, data, idade, endereco))
                    print("\n\tPessoa adicionada com sucesso.")
                    stop()
                except:
                    print("\n\tFalha ao adicionar pessoa.")
                    stop()
            connection.commit()
        finally:
            connection.close()

def read():
    tab = input("\n\n\n\tNome da tabela para leitura: ")
    print("\n\tVer tabela completa - 1\n\n\tUsar condição WHERE - 2")
    opc = input("Opção: ")
    cls()

    if opc == "1":
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM " + tab + ";"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
            
                    print("\n\nCpf\tNome\tSobrenome\tData\tIdade\tEndereco")
                    print("---------------------------------------------------------------------------")
                    for row in result:
                        print(row)
                    stop()
                except:
                    print("\n\tFalha ao ler tabela.")
                    stop()
            connection.commit()
        finally:
            connection.close()
    else:
        cond = input("\n\n\tEscreva a condição usando sintaxe SQL.\n\nSELECT * FROM " + tab + "\nWHERE ")

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM " + tab + " WHERE " + cond + ";"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
            
                    print("\n\nCpf\tNome\tSobrenome\tData\tIdade\tEndereco")
                    print("---------------------------------------------------------------------------")
                    for row in result:
                        print(row)
                    stop()
                except:
                    print("\n\tFalha ao ler tabela.")
                    stop()
            connection.commit()
        finally:
            connection.close()

def update():
    tab = input("\n\n\n\tNome da tabela onde será feita a operação UPDATE: ")
    frase = "\n\tId da tabela " + tab + " a ser atualizado: "
    n_id = input(frase)
    cls()

    if tab == "pessoa":
        print("\n\n\n\tSelecione o que atualizar:")
        print("\n\tCPF - 1\n\tNome - 2\n\tSobrenome - 3\n\tData - 4\n\tIdade - 5\n\tEndereço - 6\n\tTudo - 7\n\tFim - 0")
        opc = input("Opção: ")
        cls()
        print("\n\n\n\t")
        if opc == "1":
            cpf = input("\tCPF: ")
            frase = "cpf='" + cpf + "'"
        elif opc == "2":
            nome = input("\tNome: ")
            frase = "p_nome='" + nome + "'"
        elif opc == "3":
            sobrenome = input("\tSobrenome: ")
            frase = "u_nome='" + sobrenome + "'"
        elif opc == "4":
            data = input("\tData: ")
            frase = "data_nascimento='" + data + "'"
        elif opc == "5":
            idade = input("\tIdade: ")
            frase = "idade=" + idade
        elif opc == "6":
            endereco = input("\tEndereço: ")
            frase = "endereco='" + endereco + "'"
        elif opc == "7":
            cpf = input("\tCPF: ")
            nome = input("\tNome: ")
            sobrenome = input("\tSobrenome: ")
            data = input("\tData: ")
            idade = input("\tIdade: ")
            endereco = input("\tEndereço: ")
            frase = "cpf='" + cpf + "', p_nome='" + nome + "', u_nome='" + sobrenome + "', data_nascimento='" + data + "', idade=" + idade + ", endereco='" + endereco + "'"
           
        if opc != "0":
            try:
                with connection.cursor() as cursor:
                    sql = "UPDATE " + tab + " SET " + frase + " WHERE id_" + tab + "= %s;"
                    try:
                        cursor.execute(sql, (n_id))
                        print("\n\t" + tab.capitalize() + " atualizada com sucesso.")
                        stop()
                    except:
                        print("\n\tFalha ao atualizar " + tab + ".")
                        stop()
                
                connection.commit()
            finally:
                connection.close()

def delete():
    tab = input("\n\n\n\tNome da tabela onde será feita a operação DELETE: ")
    print("\n\tDeletar a tabela - 1\n\n\tDeletar linha na tabela - 2")
    opc = input("Opção: ")
    cls()

    if opc == "2":
        frase = "\n\tId do(a) " + tab + " a ser deletado: "
        n_id = input(frase)

        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM " + tab + " WHERE id_" + tab + "= %s;"
                try:
                    cursor.execute(sql, (n_id))
                    print("\n\t" + tab.capitalize() + " deletada com sucesso.")
                    stop()
                except:
                    print("\n\tFalha ao deletar " + tab + ".")
                    stop()        
            connection.commit()
        finally:
            connection.close()
    else:
        try:
            with connection.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS " + tab.upper() + ";"
                try:
                    cursor.execute(sql, (n_id))
                    print("\n\tTabela" + tab + " deletada com sucesso.")
                    stop()
                except:
                    print("\n\tFalha ao deletar tabela" + tab + ".")
                    stop()
        
            connection.commit()
        finally:
            connection.close()
opc = 10
while opc != "0":
    cls()

    print("\t\t\tCRUD para o banco de dados.\n\n")
    print("\tCREATE - 1 \n\n\tREAD - 2 \n\n\tUPDATE - 3 \n\n\tDELETE - 4 \n\n\tSair - 0")
    opc = input("Opção: ")

    cls()

    if opc == "1":
        create()
    elif opc == "2":
        read()
    elif opc == "3":
        update()
    elif opc == "4":
        delete()
