import tkinter as tk
from crud import Persistencia as per

class Application:
    def __init__(self, master=None):
        self.flag = 0
        self.fonte = ("Arial", "10")
        self.op = " "
        self.cont = tk.Frame(master)
        self.cont["pady"] = 20
        self.cont.pack()
        self.msg = tk.Label(self.cont, text="Banco de Dados para Fake News")
        self.msg["font"] = ("Arial", "10", "bold")
        self.msg.pack()

        self.cont2 = tk.Frame(master)
        self.cont2["padx"] = 50
        self.cont2.pack()

        self.cont3 = tk.Frame(None)
        self.cont3["pady"] = 10
        self.cont3.pack()

        self.cont4 = tk.Frame(None)
        self.cont4["pady"] = 0
        self.cont4.pack()

        self.cont5 = tk.Frame(None)
        self.cont5["pady"] = 0
        self.cont5.pack()

        self.cont6 = tk.Frame(None)
        self.cont6["pady"] = 0
        self.cont6.pack()

        self.cont7 = tk.Frame(None)
        self.cont7["pady"] = 0
        self.cont7.pack()

        self.cont8 = tk.Frame(None)
        self.cont8["pady"] = 0
        self.cont8.pack()

        self.cont1 = tk.Frame(None)
        self.cont1["pady"] = 10
        self.cont1.pack()

        self.erro = tk.Frame(None)
        self.erro["pady"] = 0
        self.erro.pack()

        self.create = tk.Button(self.cont2)
        self.create["text"] = "Create"
        self.create["font"] = self.fonte
        self.create["width"] = 5
        self.create["command"] = self.Create
        self.create.pack(side=tk.LEFT)

        self.read = tk.Button(self.cont2)
        self.read["text"] = "Read"
        self.read["font"] = self.fonte
        self.read["width"] = 5
        self.read["command"] = self.Read
        self.read.pack(side=tk.LEFT)

        self.update = tk.Button(self.cont2)
        self.update["text"] = "Update"
        self.update["font"] = self.fonte
        self.update["width"] = 5
        self.update["command"] = self.Update
        self.update.pack(side=tk.LEFT)

        self.delete = tk.Button(self.cont2)
        self.delete["text"] = "Delete"
        self.delete["font"] = self.fonte
        self.delete["width"] = 5
        self.delete["command"] = self.Delete
        self.delete.pack(side=tk.LEFT)

        self.voltar = tk.Button(self.cont)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = self.fonte
        self.voltar["width"] = 5
        self.voltar["command"] = self.Voltar
        self.voltar.pack()

        self.sair = tk.Button(self.cont)
        self.sair["text"] = "Sair"
        self.sair["font"] = self.fonte
        self.sair["width"] = 5
        self.sair["command"] = self.cont.quit
        self.sair.pack()

        
    def Voltar(self):
        self.cont.pack_forget()
        self.cont1.pack_forget()
        self.cont2.pack_forget()
        self.cont3.pack_forget()
        self.cont4.pack_forget()
        self.cont5.pack_forget()
        self.cont6.pack_forget()
        self.cont7.pack_forget()
        self.cont8.pack_forget()
        self.erro.pack_forget()
        Application()

    def reset(self):
        self.cont2.pack_forget()

    def Create(self):
        self.reset()
        msg = tk.Label(self.cont3, text="Create")
        msg["font"] = ("Arial", "10", "bold")
        msg.pack()
        msg2 = tk.Label(self.cont3, text="Nome Tabela: ")
        msg2.pack(side=tk.LEFT)
        self.tabela = tk.Entry(self.cont3)
        self.tabela["width"] = 30
        self.tabela["font"] = self.fonte
        self.tabela.pack(side=tk.LEFT)
        ir = tk.Button(self.cont3)
        ir["text"] = "Ir"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack()
        ir["command"] = self.checkCreate

    def checkCreate(self):
        self.op = self.tabela.get()
        if self.op == "pessoa":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            cpf = tk.Label(self.cont4, text="CPF: ")
            cpf.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            nome = tk.Label(self.cont5, text="Nome: ")
            nome.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            sobrenome = tk.Label(self.cont5, text="Sobrenome: ")
            sobrenome.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            #cont6
            data = tk.Label(self.cont6, text="Data Nascimento: ")
            data.pack(side=tk.TOP)
            self.ent4 = tk.Entry(self.cont6)
            self.ent4["width"] = 30
            self.ent4["font"] = self.fonte
            self.ent4.pack(side=tk.BOTTOM)
            #cont7
            end = tk.Label(self.cont7, text="Endereço: ")
            end.pack(side=tk.TOP)
            self.ent6 = tk.Entry(self.cont7)
            self.ent6["width"] = 30
            self.ent6["font"] = self.fonte
            self.ent6.pack(side=tk.TOP)
            ir = tk.Button(self.cont7)
            ir["text"] = "Inserir"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callInsert
        elif self.op == "regiao":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            reg = tk.Label(self.cont4, text="Nome da Região: ")
            reg.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            eleit = tk.Label(self.cont5, text="Num de eleitores: ")
            eleit.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            cand = tk.Label(self.cont5, text="Num de candidatos: ")
            cand.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            ir = tk.Button(self.cont7)
            ir["text"] = "Inserir"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callInsert
        elif self.op == "candidato":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            par = tk.Label(self.cont4, text="ID Partido: ")
            par.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            pes3 = tk.Label(self.cont5, text="ID Pessoa: ")
            pes3.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            reg2 = tk.Label(self.cont5, text="ID Regiao: ")
            reg2.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            #cont7
            car = tk.Label(self.cont7, text="Cargo: ")
            car.pack(side=tk.TOP)
            self.ent6 = tk.Entry(self.cont7)
            self.ent6["width"] = 30
            self.ent6["font"] = self.fonte
            self.ent6.pack(side=tk.BOTTOM)
            ir = tk.Button(self.cont7)
            ir["text"] = "Inserir"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callInsert
        elif self.op == "eleitor":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            pes2 = tk.Label(self.cont4, text="ID Pessoa: ")
            pes2.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            rege = tk.Label(self.cont5, text="ID Regiao: ")
            rege.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            zon = tk.Label(self.cont5, text="Zona: ")
            zon.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            #cont7
            sec = tk.Label(self.cont7, text="Seção: ")
            sec.pack(side=tk.TOP)
            self.ent6 = tk.Entry(self.cont7)
            self.ent6["width"] = 30
            self.ent6["font"] = self.fonte
            self.ent6.pack(side=tk.BOTTOM)
            ir = tk.Button(self.cont7)
            ir["text"] = "Inserir"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callInsert
        else:
            self.erro.pack_forget()
            self.erro = tk.Frame(None)
            self.erro["pady"] = 0
            self.erro.pack()
            msg = tk.Label(self.erro, text="Tabela não encontrada.")
            msg["font"] = ("Arial", "10")
            msg.pack(side=tk.TOP)

    def callInsert(self):
        if self.op == "pessoa":
            valores = self.ent1.get() + ", '" + self.ent3.get() + "', '" + self.ent2.get() + "', '" + self.ent4.get() + "', '" + self.ent6.get() + "'"
        elif self.op == "regiao":
            valores = "'" + self.ent1.get() + "', " + self.ent3.get() + ", " + self.ent2.get()
        elif self.op == "candidato":
            valores = self.ent1.get() + ", " + self.ent3.get() + ", " + self.ent2.get() + ", " + self.ent6.get()
        elif self.op == "eleitor":
            valores = self.ent1.get() + ", " + self.ent3.get() + ", '" + self.ent2.get() + "', " + self.ent6.get()
        self.cont4.pack_forget()
        self.cont5.pack_forget()
        self.cont6.pack_forget()
        self.cont7.pack_forget()
        retorno = per.insert(self, self.op, valores)
        msg = tk.Label(self.cont1, text=retorno)
        msg["font"] = ("Arial", "10", "bold")
        msg.pack(side=tk.TOP)
        ir = tk.Button(self.cont1)
        ir["text"] = "Ok"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack(side=tk.BOTTOM)
        ir["command"] = self.Voltar


    def Read(self):
        self.reset()
        msg = tk.Label(self.cont3, text="Read")
        msg["font"] = ("Arial", "10", "bold")
        msg.pack()
        msg2 = tk.Label(self.cont3, text="Nome Tabela: ")
        msg2.pack(side=tk.LEFT)
        self.tabela = tk.Entry(self.cont3)
        self.tabela["width"] = 30
        self.tabela["font"] = self.fonte
        self.tabela.pack(side=tk.LEFT)
        ir = tk.Button(self.cont3)
        ir["text"] = "Ir"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack()
        ir["command"] = self.checkRead

    def checkRead(self):
        self.op = self.tabela.get()
        if self.op == "pessoa":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId | Cpf\t|  Nome\t|\tData\t|\tEndereço\t"
        elif self.op == "regiao":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId | Região | Eleitores | Candidatos"
        elif self.op == "eleitor":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId|Id_pessoa|Id_região|Zona|Seção"
        elif self.op == "candidato":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId|Id_partido|Id_pessoa|Id_região|Id_cargo"
        elif self.op == "meio_comunicacao":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId\tId_notícia\tTipo Meio Comunicação\tData"
        elif self.op == "midia":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId\tId_notícia\tTipo da mídia\tNome arquivo\tTamanho\tFormato"
        elif self.op == "noticia":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId\tData publicação\tTítulo\tTexto"
        elif self.op == "partido":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId\tRegião\tNome partido\tSigla\tData"
        elif self.op == "cargo_politico":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            frase = "\n\nId\tId_candidato\tCargo"
        else:
            self.erro.pack_forget()
            self.erro = tk.Frame(None)
            self.erro["pady"] = 0
            self.erro.pack()
            msg = tk.Label(self.erro, text="Tabela não encontrada.")
            msg["font"] = ("Arial", "10")
            msg.pack(side=tk.TOP)
        msg = tk.Label(self.cont4, text=frase)
        msg["font"] = ("Arial", "10", "bold")
        msg.pack()
        result = per.select(self, self.op)
        for row in result:
            msg1 = tk.Label(self.cont5, text=row)
            msg1["font"] = ("Arial", "10")
            msg1.pack(side=tk.TOP)
        ir = tk.Button(self.cont1)
        ir["text"] = "Ok"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack(side=tk.BOTTOM)
        ir["command"] = self.Voltar
    
    def Update(self):
        self.reset()
        msg = tk.Label(self.cont3, text="Update")
        msg["font"] = ("Arial", "10", "bold")
        msg.pack()
        msg2 = tk.Label(self.cont3, text="Nome Tabela: ")
        msg2.pack(side=tk.LEFT)
        self.tabela = tk.Entry(self.cont3)
        self.tabela["width"] = 30
        self.tabela["font"] = self.fonte
        self.tabela.pack(side=tk.LEFT)
        msg3 = tk.Label(self.cont1, text="n_Id:")
        msg3.pack(side=tk.LEFT)
        self.id = tk.Entry(self.cont1)
        self.id["width"] = 30
        self.id["font"] = self.fonte
        self.id.pack(side=tk.LEFT)
        ir = tk.Button(self.cont3)
        ir["text"] = "Ir"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack()
        ir["command"] = self.checkUpdate
    
    def checkUpdate(self):
        self.op = self.tabela.get()
        self.aux = tk.Entry(self.cont4)
        self.aux["width"] = 30
        self.aux["font"] = self.fonte
        self.aux.pack(side=tk.RIGHT)
        self.vazio = self.aux.get()
        self.aux.pack_forget()
        if self.op == "pessoa":
            self.cont3.pack_forget()
            self.cont1.pack_forget()
            self.erro.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            cpf = tk.Label(self.cont4, text="CPF: ")
            cpf.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            nome = tk.Label(self.cont5, text="Nome: ")
            nome.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.TOP)
            sobrenome = tk.Label(self.cont5, text="Sobrenome: ")
            sobrenome.pack(side=tk.TOP)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            #cont6
            data = tk.Label(self.cont6, text="Data: ")
            data.pack(side=tk.TOP)
            self.ent4 = tk.Entry(self.cont6)
            self.ent4["width"] = 30
            self.ent4["font"] = self.fonte
            self.ent4.pack(side=tk.BOTTOM)
            #cont7
            end = tk.Label(self.cont7, text="Endereço: ")
            end.pack(side=tk.TOP)
            self.ent6 = tk.Entry(self.cont7)
            self.ent6["width"] = 30
            self.ent6["font"] = self.fonte
            self.ent6.pack(side=tk.TOP)
            ir = tk.Button(self.cont7)
            ir["text"] = "Atualizar"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callUpdate
        elif self.op == "regiao":
            self.cont3.pack_forget()
            self.cont1.pack_forget()
            self.erro.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            reg = tk.Label(self.cont4, text="Nome da Região: ")
            reg.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            eleit = tk.Label(self.cont5, text="Num de eleitores: ")
            eleit.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            cand = tk.Label(self.cont5, text="Num de candidatos: ")
            cand.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            ir = tk.Button(self.cont7)
            ir["text"] = "Atualizar"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callUpdate
        elif self.op == "candidato":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            self.cont1.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            par = tk.Label(self.cont4, text="ID Partido: ")
            par.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            pes3 = tk.Label(self.cont5, text="ID Pessoa: ")
            pes3.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            reg2 = tk.Label(self.cont5, text="ID Regiao: ")
            reg2.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            #cont7
            car = tk.Label(self.cont7, text="Cargo: ")
            car.pack(side=tk.TOP)
            self.ent6 = tk.Entry(self.cont7)
            self.ent6["width"] = 30
            self.ent6["font"] = self.fonte
            self.ent6.pack(side=tk.BOTTOM)
            ir = tk.Button(self.cont7)
            ir["text"] = "Atualizar"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callUpdate
        elif self.op == "eleitor":
            self.cont3.pack_forget()
            self.erro.pack_forget()
            self.cont1.pack_forget()
            #cont4
            msg = tk.Label(self.cont4, text="Create")
            msg["font"] = ("Arial", "10", "bold")
            msg.pack(side=tk.TOP)
            pes2 = tk.Label(self.cont4, text="ID Pessoa: ")
            pes2.pack(side=tk.TOP)
            self.ent1 = tk.Entry(self.cont4)
            self.ent1["width"] = 30
            self.ent1["font"] = self.fonte
            self.ent1.pack(side=tk.RIGHT)
            #cont5
            rege = tk.Label(self.cont5, text="ID Regiao: ")
            rege.pack(side=tk.TOP)
            self.ent2 = tk.Entry(self.cont5)
            self.ent2["width"] = 30
            self.ent2["font"] = self.fonte
            self.ent2.pack(side=tk.BOTTOM)
            zon = tk.Label(self.cont5, text="Zona: ")
            zon.pack(side=tk.BOTTOM)
            self.ent3 = tk.Entry(self.cont5)
            self.ent3["width"] = 30
            self.ent3["font"] = self.fonte
            self.ent3.pack(side=tk.BOTTOM)
            #cont7
            sec = tk.Label(self.cont7, text="Seção: ")
            sec.pack(side=tk.TOP)
            self.ent6 = tk.Entry(self.cont7)
            self.ent6["width"] = 30
            self.ent6["font"] = self.fonte
            self.ent6.pack(side=tk.BOTTOM)
            ir = tk.Button(self.cont7)
            ir["text"] = "Atualizar"
            ir["font"] = self.fonte
            ir["width"] = 5
            ir.pack(side=tk.BOTTOM)
            ir["command"] = self.callUpdate
        else:
            self.erro.pack_forget()
            self.erro = tk.Frame(None)
            self.erro["pady"] = 0
            self.erro.pack()
            msg = tk.Label(self.erro, text="Tabela não encontrada.")
            msg["font"] = ("Arial", "10")
            msg.pack(side=tk.TOP)
    
    def callUpdate(self):
        valores = ""
        if self.op == "pessoa":
            if self.ent1.get() != self.vazio:
                valores = valores + "cpf='" + self.ent1.get() + "', "
            if self.ent2.get() != self.vazio:
                valores = valores + "p_nome='" + self.ent2.get() + "', "
            if self.ent3.get() != self.vazio:
                valores = valores + "u_nome='" + self.ent3.get() + "', "
            if self.ent4.get() != self.vazio:
                valores = valores + "data_nascimento='" + self.ent4.get() + "', "
            if self.ent6.get() != self.vazio:
                valores = valores + "endereco='" + self.ent6.get() + "', "
        elif self.op == "regiao":
            if self.ent1.get() != self.vazio:
                valores = valores + "nome_regiao='" + self.ent1.get() + "', "
            if self.ent2.get() != self.vazio:
                valores = valores + "num_eleitores='" + self.ent3.get() + "', "
            if self.ent3.get() != self.vazio:
                valores = valores + "num_candidatos='" + self.ent2.get() + "', "
        elif self.op == "candidato":
            if self.ent1.get() != self.vazio:
                valores = valores + "id_partido='" + self.ent1.get() + "', "
            if self.ent2.get() != self.vazio:
                valores = valores + "id_pessoa='" + self.ent3.get() + "', "
            if self.ent3.get() != self.vazio:
                valores = valores + "id_regiao='" + self.ent2.get() + "', "
            if self.ent6.get() != self.vazio:
                valores = valores + "id_cargo='" + self.ent6.get() + "', "
        elif self.op == "eleitor":
            if self.ent1.get() != self.vazio:
                valores = valores + "id_pessoa='" + self.ent1.get() + "', "
            if self.ent2.get() != self.vazio:
                valores = valores + "id_regiao='" + self.ent3.get() + "', "
            if self.ent3.get() != self.vazio:
                valores = valores + "zona='" + self.ent2.get() + "', "
            if self.ent6.get() != self.vazio:
                valores = valores + "secao='" + self.ent6.get() + "', "

        valores = valores[:-2]
        self.cont4.pack_forget()
        self.cont5.pack_forget()
        self.cont6.pack_forget()
        self.cont7.pack_forget()
        retorno = per.update(self, self.op, valores, self.id.get())
        msg = tk.Label(self.cont8, text=retorno)
        msg["font"] = ("Arial", "10", "bold")
        msg.pack(side=tk.TOP)
        ir = tk.Button(self.cont8)
        ir["text"] = "Ok"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack(side=tk.BOTTOM)
        ir["command"] = self.Voltar

    def Delete(self):
        self.reset()
        msg = tk.Label(self.cont3, text="Delete")
        msg["font"] = ("Arial", "10", "bold")
        msg.pack()
        msg2 = tk.Label(self.cont3, text="Apagar Tabela: ")
        msg2.pack(side=tk.LEFT)
        self.tabela = tk.Entry(self.cont3)
        self.tabela["width"] = 30
        self.tabela["font"] = self.fonte
        self.tabela.pack(side=tk.LEFT)
        msg3 = tk.Label(self.cont1, text="Apagar o n_Id:")
        msg3.pack(side=tk.LEFT)
        self.id = tk.Entry(self.cont1)
        self.id["width"] = 30
        self.id["font"] = self.fonte
        self.id.pack(side=tk.LEFT)
        ir = tk.Button(self.cont3)
        ir["text"] = "Tabela"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack()
        ir["command"] = self.checkDelete
        ir2 = tk.Button(self.cont1)
        ir2["text"] = "Id"
        ir2["font"] = self.fonte
        ir2["width"] = 5
        ir2.pack()
        ir2["command"] = self.checkDeleteId

    def checkDelete(self):
        self.op = self.tabela.get()
        retorno = per.drop(self, self.op)
        self.cont3.pack_forget()
        self.cont1.pack_forget()
        msg = tk.Label(self.cont8, text=retorno)
        msg["font"] = ("Arial", "10", "bold")
        msg.pack(side=tk.TOP)
        ir = tk.Button(self.cont8)
        ir["text"] = "Ok"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack(side=tk.BOTTOM)
        ir["command"] = self.Voltar


    def checkDeleteId(self):
        self.op = self.tabela.get()
        retorno = per.delete(self, self.op, self.id.get())
        self.cont3.pack_forget()
        self.cont1.pack_forget()
        msg = tk.Label(self.cont8, text=retorno)
        msg["font"] = ("Arial", "10", "bold")
        msg.pack(side=tk.TOP)
        ir = tk.Button(self.cont8)
        ir["text"] = "Ok"
        ir["font"] = self.fonte
        ir["width"] = 5
        ir.pack(side=tk.BOTTOM)
        ir["command"] = self.Voltar

root = tk.Tk()
root.title("CRUD")
Application(root)
root.mainloop()