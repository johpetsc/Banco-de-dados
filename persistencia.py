import pymysql

connection = pymysql.connect(
            host='localhost',
            user='root',
            password='palavra',
            db='trabalhobd',
        )

class Persistencia:
    def insert(self, tab, valores):
        if tab == "pessoa":
            frase = "cpf, p_nome, u_nome, data_nascimento, endereco"
        elif tab == "regiao":
            frase = "nome_regiao, num_eleitores, num_candidatos"
        elif tab == "candidato":
            frase = "id_pessoa, id_regiao"
        elif tab == "eleitor":
            frase = "id_pessoa, id_regiao, zona, secao"
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO " + tab + " (" + frase + ") VALUES (" + valores + ");"
                print(sql)
                try:
                    cursor.execute(sql)
                    print("\n\t" + tab.capitalize() + " adicionada com sucesso.")
                except:
                    print("\n\tFalha ao adicionar " + tab + ".")
                connection.commit()
        finally:
            connection.close()

    def select(self, tab):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM " + tab + ";"
                print(sql)
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                except:
                    print("\n\tFalha ao ler tabela.")
            connection.commit()
        finally:
            connection.close()
        return result
    
    def update(self, tab, frase, n_id):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE " + tab + " SET " + frase + " WHERE id_" + tab + "= %s;"
                print(sql, (n_id))
                try:
                    cursor.execute(sql, (n_id))
                    print("\n\t" + tab.capitalize() + " atualizada com sucesso.")
                except:
                    print("\n\tFalha ao atualizar " + tab + ".")             
            connection.commit()
        finally:
            connection.close()
    
    def drop(self, tab):
        try:
            with connection.cursor() as cursor:
                sql = "DROP TABLE IF EXISTS " + tab.upper() + ";"
                print(sql)
                try:
                    cursor.execute(sql)
                    print("\n\tTabela" + tab + " deletada com sucesso.")
                except:
                    print("\n\tFalha ao deletar tabela " + tab + ".")
        
            connection.commit()
        finally:
            connection.close()
    
    def delete(self, tab, n_id):
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM " + tab + " WHERE id_" + tab + "= %s;"
                print(sql, (n_id))
                try:
                    cursor.execute(sql, (n_id))
                    print("\n\t" + tab.capitalize() + " deletada com sucesso.")
                except:
                    print("\n\tFalha ao deletar " + tab + ".")   
            connection.commit()
        finally:
            connection.close()