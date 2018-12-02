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
        frase = "cpf, p_nome, u_nome, data_nascimento, idade, endereco"
        valores = cpf + ", " + nome + ", " + sobrenome + ", " + data + ", " + idade + ", " + endereco
    elif tab == "regiao":
        reg = input("\tNome da Região: ")
        num_e = input("\tNúmero de eleitores: ")
        num_c = input("\tNúmero de candidatos: ")
        frase = "nome_regiao, num_eleitores, num_candidatos"
        valores = reg + ", " + num_e + ", " + num_c
    elif tab == "candidato":
        id_p = input("\tId Pessoa: ")
        id_r = input("\tId Região: ")
        frase = "id_pessoa, id_regiao"
        valores = id_p + ", " + ir_r
    elif tab == "eleitor":
        id_p = input("\tId Pessoa: ")
        id_r = input("\tId Região: ")
        zon = input("\tZona: ")
        sec = input("\tSeção: ")
        frase = "id_pessoa, id_regiao, zona, secao"
        valores = id_p + ", " + id_r + ", " + zon + ", " + sec
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO " + tab + " (" + frase + ") VALUES (" + valores + ");"
            try:
                cursor.execute(sql)
                print("\n\t" + tab.capitalize() + " adicionada com sucesso.")
                stop()
            except:
                print("\n\tFalha ao adicionar " + tab + ".")
                stop()
        connection.commit()
    finally:
        connection.close()

def read():
    tab = input("\n\n\n\tNome da tabela para leitura: ")
    print("\n\tVer tabela completa - 1\n\n\tUsar condição WHERE - 2")
    opc = input("Opção: ")
    cls()

    if tab == "pessoa":
        frase = "\n\nId\tCpf\tNome\tSobrenome\tData\tIdade\tEndereço"
    elif tab == "regiao":
        frase = "\n\nId\tRegião\tEleitores\tCandidatos"
    elif tab == "eleitor":
        frase = "\n\nId\tId_pessoa\tId_região\tZona\tSeção"
    elif tab == "candidato":
        frase = "\n\nId\tId_pessoa\tId_região"
    elif tab == "foto":
        frase = "\n\nId\tId_pessoa\tFoto\tTamanho\tFormato"
    elif tab == "meio_comunicacao":
        frase = "\n\nId\tId_notícia\tTipo Meio Comunicação\tData"
    elif tab == "midia":
        frase = "\n\nId\tId_notícia\tTipo da mídia\tNome arquivo\tTamanho\tFormato"
    elif tab == "noticia":
        frase = "\n\nId\tData publicação\tTítulo\tTexto"
    elif tab == "partido":
        frase = "\n\nId\tRegião\tNome partido\tSigla\tData"
    elif tab == "cargo_politico":
        frase = "\n\nId\tId_candidato\tCargo"

    if opc == "1":
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM " + tab + ";"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
            
                    print(frase)
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
            
                    print(frase)
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
    
    elif tab == "regiao":
        print("\n\n\n\tSelecione o que atualizar:")
        print("\n\tNome da Região - 1\n\tNúmero de eleitores - 2\n\tNúmero de candidatos - 3\n\tTudo - 4\n\tFim - 0")
        opc = input("Opção: ")
        cls()
        print("\n\n\n\t")
        if opc == "1":
            reg = input("\tNome da Região: ")
            frase = "nome_regiao='" + rege + "'"
        elif opc == "2":
            num_e = input("\tNúmero de eleitores: ")
            frase = "num_eleitores='" + num_e + "'"
        elif opc == "3":
            num_c = input("\tNúmero de candidatos: ")
            frase = "num_candidatos='" + num_c + "'"
        elif opc == "4":
            reg = input("\tNome da Região: ")
            num_e = input("\tNúmero de eleitores: ")
            num_c = input("\tNúmero de candidatos: ")
            frase = "nome_regiao='" + rege + "', num_eleitores='" + num_e + "', num_candidatos='" + num_c + "'"
    elif tab == "eleitor":
        print("\n\n\n\tSelecione o que atualizar:")
        print("\n\tId Pessoa - 1\n\tId Região - 2\n\tZona - 3\n\tSeção - 4\n\tTudo - 5\n\tFim - 0")
        opc = input("Opção: ")
        cls()
        print("\n\n\n\t")
        if opc == "1":
            id_p = input("\tId Pessoa: ")
            frase = "id_pessoa='" + id_p + "'"
        elif opc == "2":
            id_r = input("\tId Região: ")
            frase = "id_regiao='" + id_r + "'"
        elif opc == "3":
            zon = input("\tZona: ")
            frase = "zona='" + zon + "'"
        elif opc == "4":
            sec = input("\tSeção: ")
            frase = "secao='" + sec + "'"
        elif opc == "5":
            id_p = input("\tId Pessoa: ")
            id_r = input("\tId Região: ")
            zon = input("\tZona: ")
            sec = input("\tSeção: ")
            frase = "id_pessoa='" + id_p + "', id_regiao='" + id_r + "', zona='" + zon + "'secao='" + sec + "'"
    elif tab == "candidato":
        print("\n\n\n\tSelecione o que atualizar:")
        print("\n\tId Pessoa - 1\n\tId Região - 2\n\tTudo - 3\n\tFim - 0")
        opc = input("Opção: ")
        cls()
        print("\n\n\n\t")
        if opc == "1":
            id_p = input("\tId Pessoa: ")
            frase = "id_pessoa='" + id_p + "'"
        elif opc == "2":
            id_r = input("\tId Região: ")
            frase = "id_regiao='" + id_r + "'"
        elif opc == "3":
            id_p = input("\tId Pessoa: ")
            id_r = input("\tId Região: ")
            frase = "id_pessoa='" + id_p + "', id_regiao='" + id_r + "'"      
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
