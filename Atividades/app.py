from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
 
 

janela = Tk()

class relatorios():
    # Função para gerar o relatório em PDF
    def gerar_relatorio_pdf(self, os):
        # Consulta ao banco de dados para obter os dados relevantes para a OS fornecida
        self.conecta_bd()
        consulta = self.cursor.execute("""
            SELECT produtos, SUM(CASE WHEN tipo = 'S' THEN quantidade ELSE 0 END) AS saida,
            SUM(CASE WHEN tipo = 'D' THEN quantidade ELSE 0 END) AS devolucao
            FROM Requisicoes WHERE os = ? GROUP BY produtos
        """, (os,))
        dados = consulta.fetchall()
        self.desconecta_bd()

        # Inicialização do PDF
        pdf_file = "relatorio_{}.pdf".format(os)
        pdf = SimpleDocTemplate(pdf_file, pagesize=A4)
        story = []


        # Obtém estilos de amostra
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='CustomTitle', fontSize=16, alignment=1, spaceAfter=50, bold=True))
        styles.add(ParagraphStyle(name='CustomNormal', fontSize=12, alignment=0))

        # Cabeçalho do relatório
        header = "Confronto saida x devolução".format(os)
        story.append(Paragraph(header, styles['CustomTitle']))

        # Tabela com os dados
        table_data = [["PRODUTO", "SAIDA", "DEVOLUÇÃO", "SALDO"]]
        for produto, saida, devolucao in dados:
            restante = saida - devolucao
            table_data.append([produto, saida, devolucao, restante])

        # Adiciona cores ao cabeçalho e às linhas da tabela
        header_style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
        ]

        row_style = [
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightyellow),  # Cor de fundo das linhas
            ('TEXTCOLOR', (1, 1), (-1, -1), colors.black),  # Cor do texto das linhas
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),  # Alinhamento do texto das linhas
            ('FONTNAME', (1, 1), (-1, -1), 'Times-Roman')  # Fonte do texto das linhas
        ]

        table_data = Table(table_data, colWidths=[310, 80, 80, 80])
        table_data.setStyle(TableStyle(header_style))
        table_data.setStyle(TableStyle(row_style))

        story.append(table_data)

        # Geração do PDF
        pdf.build(story)

        # Abrir o PDF após a criação
        webbrowser.open(pdf_file)
        


class funcoes():

    def marcar_saida_devolucao(self):
        if self.saida_var.get() == 1:  # Verifica se a checkbutton 'SAIDA' está marcada
            self.saida_requis_entry.delete(0, END)  # Limpa o conteúdo da entrada 'saida_requis'
            self.saida_requis_entry.insert(END, "S")  # Insere "S" na entrada 'saida_requis'
        elif self.devolucao_var.get() == 1:  # Verifica se a checkbutton 'DEVOLUÇÃO' está marcada
            self.saida_requis_entry.delete(0, END)  # Limpa o conteúdo da entrada 'saida_requis'
            self.saida_requis_entry.insert(END, "D")  # Insere "D" na entrada 'saida_requis'
        else:
            self.saida_requis_entry.delete(0, END)  # Limpa o conteúdo da entrada 'saida_requis'
    #ESSA FUNÇÃO LIMPA AS ENTRYS(CAMPOS) INSERIDOS NA TABELA"NA PRIMEIRA TELA ONDE É INFORMADO OS DADOS DA REQUISIÇÃO COMO POR EXEMPLO OS, CODIGO E NOME DA FAZENDA...
    def limpa_requisicao(self):
        self.id = self.sequenci_Entry.delete(0, END)
        self.data = self.data_entry.delete(0, END)
        self.saida_requis = self.saida_requis_entry.delete(0, END)
        self.cod_fazenda_entry.delete(0, END)
        self.nome_fazenda_entry.delete(0, END)
        self.almox_entry.delete(0, END)
        self.filial_entry.delete(0, END)
        self.os_entry.delete(0, END)
        self.operacao_entry.delete(0, END)
        self.cultura_combo.delete(0, END)
        self.cod_responsavel_entry.delete(0, END)
        self.nome_responsavel_entry.delete(0, END)
        self.cod_produto_1.delete(0, END)
        self.nome_produto_entry.delete(0, END)
        self.quantidade_entry_1.delete(0, END)
        self.unidade_entry_1.delete(0, END)
    #CONECTA AO BANCO DE DADOS
    def conecta_bd(self):
        self.conn = sqlite3.connect("Requisicoes_insumos.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    #DESCONECTA DO BANCO DE DADOS
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    #CRIA AS COLUNAS DA TABELA
    def montaTabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Requisicoes (
                ID INTEGER PRIMARY KEY NOT NULL,
                tipo text(4) NOT NULL,
                cod_fazenda INTEGER(5) NOT NULL,
                nome_fazenda TEXT(25) NOT NULL,
                almoxarifado CHAR(25) NOT NULL,
                filial CHAR(25) NOT NULL,
                os INTEGER(20) NOT NULL,
                operacao CHAR(50) NOT NULL,
                cultura CHAR(20) NOT NULL,
                cod_responsavel INTEGER(2) NOT NULL,
                nome_responsavel TEXT(30) NOT NULL,
                cod_produto INTEGER(6) NOT NULL,
                produtos CHAR(40) NOT NULL,
                quantidade INTEGER(5) NOT NULL,
                unidade CHAR(3),
                data INTEGER(10)
            );
        """)
        self.conn.commit()
        print("Banco de dados criado")
        self.desconecta_bd()
    #ESSA FUNÇÃO FOI CRIADA PARA QUE SEJA UTILIZADA APENAS PARA FACILITAR A CRIAÇÃO DE OUTRAS FUNÇÕES QUE TERÃO OS MESMOS MÉTODOS.
    def variaveis(self):
        self.id = self.sequenci_Entry.get()
        self.data = self.data_entry.get()
        self.saida_requis = self.saida_requis_entry.get()
        self.cod_fazenda = self.cod_fazenda_entry.get()
        self.nome_fazenda = self.nome_fazenda_entry.get()
        self.almoxarifado = self.almox_entry.get()
        self.filial = self.filial_entry.get()
        self.os = self.os_entry.get()
        self.operacao = self.operacao_entry.get()
        self.cultura = self.cultura_combo.get()
        self.cod_responsavel = self.cod_responsavel_entry.get()
        self.nome_responsavel = self.nome_responsavel_entry.get()
        self.cod_produto = self.cod_produto_1.get()
        self.produtos = self.nome_produto_entry.get()
        self.quantidade = self.quantidade_entry_1.get()
        self.unidade = self.unidade_entry_1.get()
        

    def salvar(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""
            INSERT INTO Requisicoes (tipo, cod_fazenda, nome_fazenda, almoxarifado, filial, os,
            operacao, cultura, cod_responsavel, nome_responsavel, cod_produto, produtos, quantidade,
            unidade, data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.saida_requis, self.cod_fazenda, self.nome_fazenda, self.almoxarifado, self.filial, self.os,
            self.operacao, self.cultura, self.cod_responsavel, self.nome_responsavel, self.cod_produto,
            self.produtos, self.quantidade, self.unidade, self.data))
        self.conn.commit()
        print("Dados inseridos com sucesso!")
        self.desconecta_bd()
        self.limpa_requisicao()
        self.select_lista()

    def select_lista(self):
        self.lista_requi.delete(*self.lista_requi.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT id, tipo, os, operacao, cod_fazenda, nome_fazenda, cultura, cod_produto, produtos, quantidade, unidade, cod_responsavel, nome_responsavel, data FROM Requisicoes
        ORDER BY os DESC; """)
        for i in lista:
            self.lista_requi.insert("", END, values=i)
        self.desconecta_bd()
    #IMPLEMENTA A FUNÇAO DE SELEÇÃO COM DOIS CLICKS NA LISTA TREEVIEW
    def onDoubleClick(self, event):
        self.limpa_requisicao()
        self.lista_requi.selection()

        for n in self.lista_requi.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = self.lista_requi.item(n, 'values')
            self.sequenci_Entry.insert(END, col1)
            self.saida_requis_entry.insert(END, col2)
            self.os_entry.insert(END, col3)
            self.operacao_entry.insert(END, col4)
            self.cod_fazenda_entry.insert(END, col5)
            self.nome_fazenda_entry.insert(END, col6)
            self.cultura_combo.insert(END, col7)
            self.cod_produto_1.insert(END, col8)
            self.nome_produto_entry.insert(END, col9)
            self.quantidade_entry_1.insert(END, col10)
            self.unidade_entry_1.insert(END, col11)
            self.cod_responsavel_entry.insert(END, col12)
            self.nome_responsavel_entry.insert(END, col13)
            self.data_entry.insert(END, col14)
    #Exclui dados salvos na lista treeview
    def deleta_requisicao(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM Requisicoes WHERE id = ? """, (self.id,))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()

    def altera_requisicao(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE Requisicoes SET tipo = ?, os = ?, operacao = ?, cod_fazenda = ?, nome_fazenda = ?, cultura = ?, cod_produto = ?, produtos = ?, quantidade = ?,
        unidade = ?, cod_responsavel = ?, nome_responsavel = ? WHERE id = ? """, (self.saida_requis, self.os, self.operacao, self.cod_fazenda, self.nome_fazenda, self.cultura, self.cod_produto, self.produtos,
        self.quantidade, self.unidade, self.cod_responsavel, self.nome_responsavel, self.id))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()


class Application(funcoes, relatorios):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_de_tela()
        self.criar_campos()
        self.carregar_dados()
        self.carregar_dados_responsavel()
        self.carregar_dados_produtos()
        self.criar_botoes()
        self.lista_requisicao()
        self.montaTabelas()
        self.select_lista()
        self.preencher_data()
        self.marcar_saida_devolucao()
        self.Menu()
        janela.mainloop()

    def tela(self):
        self.janela.title("REQUISIÇÃO DE INSUMOS")
        self.janela.configure(background='#1e3743')
        self.janela.geometry('800x500')
        self.janela.resizable(True, True)

    def frames_de_tela(self):
        self.frame_1 = Frame(self.janela)
        self.frame_1.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.12)

        self.frame_2 = Frame(self.janela)
        self.frame_2.place(relx=0.02, rely=0.14, relwidth=0.96, relheight=0.20)

        self.frame_3 = Frame(self.janela)
        self.frame_3.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.20)

        self.frame_4 = Frame(self.janela)
        self.frame_4.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.35)

    def criar_botoes(self):
        self.btlimpar = Button(self.frame_3, text="LIMPAR", font=("Verdana", "10"), width=10, bg="#90EE90", command=self.limpa_requisicao)
        self.btlimpar.place(relx=0.02, rely=0.70)

        self.btalterar = Button(self.frame_3, text="ALTERAR", font=("Verdana", "10"), width=10, bg="#90EE90", command=self.altera_requisicao)
        self.btalterar.place(relx=0.15, rely=0.70)

        self.btaddadicionar = Button(self.frame_3, text="ADICIONAR", font=("Verdana", "10"), width=10, bg="#90EE90", command=self.salvar)
        self.btaddadicionar.place(relx=0.28, rely=0.70)

        self.btgerar = Button(self.frame_3, text="DELETAR", font=("Verdana", "10"), width=10, bg="#f0f0f0", command=self.deleta_requisicao)
        self.btgerar.place(relx=0.70, rely=0.70)
    #LISTA DA TREEVIEW
    def lista_requisicao(self):
        self.lista_requi = ttk.Treeview(self.frame_4, height= 3, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14"))

        self.lista_requi.heading("#0", text="")
        self.lista_requi.heading("#1", text="ID")
        self.lista_requi.heading("#2", text="TIPO")
        self.lista_requi.heading("#3", text="OS")
        self.lista_requi.heading("#4", text="OPERAÇÃO")
        self.lista_requi.heading("#5", text="COD FAZ")
        self.lista_requi.heading("#6", text="FAZENDA")
        self.lista_requi.heading("#7", text="CULTURA")
        self.lista_requi.heading("#8", text="COD PROD")
        self.lista_requi.heading("#9", text="PRODUTOS")
        self.lista_requi.heading("#10", text="Qtd")
        self.lista_requi.heading("#11", text="Un")
        self.lista_requi.heading("#12", text="COD RESP")
        self.lista_requi.heading("#13", text="RESPONSAVEL")
        self.lista_requi.heading("#14", text="DATA")

        self.lista_requi.column("#0", width=1)
        self.lista_requi.column("#1", width=1)
        self.lista_requi.column("#2", width=1)
        self.lista_requi.column("#3", width=2)
        self.lista_requi.column("#4", width=120)
        self.lista_requi.column("#5", width=5)
        self.lista_requi.column("#6", width=120)
        self.lista_requi.column("#7", width=100)
        self.lista_requi.column("#8", width=5)
        self.lista_requi.column("#9", width=100)
        self.lista_requi.column("#10", width=10)
        self.lista_requi.column("#11", width=5)
        self.lista_requi.column("#12", width=5)
        self.lista_requi.column("#13", width=75)
        self.lista_requi.column("#14", width=10)

        self.lista_requi.place(relx= 0.01, rely= 0.01, relwidth= 0.98, relheight= 0.80)
        self.lista_requi.bind("<Double-1>", self.onDoubleClick)

    def criar_campos(self):
        self.titulo = Label(self.frame_1, text="FICHA DE RETIRADA DE INSUMO", font=("Algerian", 14))
        self.titulo.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5)

        self.sequencia = Label(self.frame_1, text="ID:", font=("colibri", 10))
        self.sequencia.place(relx=0.02, rely=0.3, relwidth=0.05)

        self.sequenci_Entry = Entry(self.frame_1)
        self.sequenci_Entry.place(relx=0.12, rely=0.3, relwidth=0.09)

        self.saida_requis_entry = Entry(self.frame_1)
        self.saida_requis_entry.place(relx= 0.07, rely= 0.3, relwidth= 0.04)        

        self.lb_data = Label(self.frame_1, text="DATA")
        self.lb_data.place(relx= 0.70, rely= 0.3, relwidth= 0.05)

        self.data_entry = Entry(self.frame_1)
        self.data_entry.place(relx= 0.76, rely= 0.3, relwidth= 0.2)

        self.cod_faz = Label(self.frame_2, text="COD. FAZENDA")
        self.cod_faz.place(relx=0.0001, rely=0.10)

        self.cod_fazenda_entry = Entry(self.frame_2)
        self.cod_fazenda_entry.place(relx=0.13, rely=0.10, relwidth=0.05)
        self.cod_fazenda_entry.bind("<Tab>", self.preencher_nome_fazenda)

        self.nome_faz = Label(self.frame_2, text="NOME DA FAZENDA :")
        self.nome_faz.place(relx=0.18, rely=0.10)

        self.nome_fazenda_entry = Entry(self.frame_2)
        self.nome_fazenda_entry.place(relx=0.35, rely=0.10, relwidth=0.4)

        self.almox = Label(self.frame_2, text="ALMOX :")
        self.almox.place(relx=0.6, rely=0.10, relwidth=0.10)

        self.almox_entry = Entry(self.frame_2)
        self.almox_entry.place(relx=0.7, rely=0.10, relwidth=0.28)

        self.os = Label(self.frame_2, text="OS:")
        self.os.place(relx=0.045, rely=0.35, relwidth=0.1)
        
        self.os_entry = Entry(self.frame_2)
        self.os_entry.place(relx=0.13, rely=0.35, relwidth=0.05)

        self.operacao = Label(self.frame_2, text="OPERACAO :")
        self.operacao.place(relx=0.20, rely=0.35, relwidth=0.10)
        
        self.operacao_entry = Entry(self.frame_2)
        self.operacao_entry.place(relx=0.30, rely=0.35, relwidth=0.30)

        self.filial = Label(self.frame_2, text="FILIAL :")
        self.filial.place(relx=0.6, rely=0.35, relwidth= 0.10)

        self.filial_entry = Entry(self.frame_2)
        self.filial_entry.place(relx=0.7, rely=0.35, relwidth=0.28)
        
        self.responsavel = Label(self.frame_2, text="RESPONSÁVEL :")
        self.responsavel.place(relx=0.02, rely=0.60, relwidth=0.1)
        
        self.cod_responsavel_entry = Entry(self.frame_2)
        self.cod_responsavel_entry.place(relx=0.13, rely=0.60, relwidth=0.05)
        self.cod_responsavel_entry.bind("<Tab>", self.preencher_nome_responsavel)

        self.nome_responsavel_entry = Entry(self.frame_2)
        self.nome_responsavel_entry.place(relx=0.20, rely=0.60, relwidth=0.40)

        self.cultura = Label(self.frame_2, text="CULTURA :")
        self.cultura.place(relx= 0.61, rely= 0.60)

        self.cultura_combo = ttk.Combobox(self.frame_2)
        self.cultura_combo.place(relx= 0.7, rely= 0.60, relwidth= 0.28)
        self.cultura_combo['values'] = ['CANA-DE-AÇUCAR', 'EUCALIPTO', 'AGROPECUARIA']

        self.produto_1 = Label(self.frame_3, text="PRODUTO :")
        self.produto_1.place(relx= 0.0001, rely= 0.10)

        self.cod_produto_1 = Entry(self.frame_3)
        self.cod_produto_1.place(relx= 0.13, rely= 0.10, relwidth= 0.05)
        self.cod_produto_1.bind("<Tab>", self.preencher_produtos)

        self.nome_produto_entry = Entry(self.frame_3)
        self.nome_produto_entry.place(relx= 0.20, rely= 0.10, relwidth= 0.4)

        self.quantidade_1 = Label(self.frame_3, text="Qtd")
        self.quantidade_1.place(relx= 0.63, rely= 0.10)

        self.quantidade_entry_1 = Entry(self.frame_3)
        self.quantidade_entry_1.place(relx= 0.67, rely= 0.10, relwidth= 0.05)

        self.unidade_entry_1 = Entry(self.frame_3)
        self.unidade_entry_1.place(relx= 0.73, rely= 0.10, relwidth= 0.04)

        self.saida_var = IntVar()
        self.saida_check = ttk.Checkbutton(self.frame_3, text="SAIDA", variable=self.saida_var, command=self.marcar_saida_devolucao)
        self.saida_check.place(relx= 0.85, rely= 0.25)

        self.devolucao_var = IntVar()
        self.devolucao_check = ttk.Checkbutton(self.frame_3, text="DEVOLUÇÃO", variable=self.devolucao_var, command=self.marcar_saida_devolucao)
        self.devolucao_check.place(relx= 0.85, rely= 0.45)


    #Carrega e preenche os campos da ficha que tenha relação com codigo. Ex: codido da fazenda ao ser digitado tras o nome da fazenda referente aquele codigo.
    def carregar_dados(self):
        dados = pd.read_excel('C:/Users/Eliom/OneDrive/Área de Trabalho/APLICATIVO/DADOS CADASTRAIS.xlsx', sheet_name="FAZENDAS")

        self.dados_dict = {}
        for index, row in dados.iterrows():
            cod_fazenda = row['COD']
            nome_fazenda = row['FUNDO AGRICOLA']
            almox = row['ALMOX']
            filial = row['FILIAL']
            self.dados_dict[int(cod_fazenda)] = {'FUNDO AGRICOLA': nome_fazenda, 'ALMOX': almox, 'FILIAL': filial}
    def preencher_nome_fazenda(self, *args):
        #Obtém o valor do campo cod_fazenda_entry      
        cod_fazenda = self.cod_fazenda_entry.get()       
        # Obtém o nome da fazenda e a filial com base no código
        fazenda_info = self.dados_dict.get(int(cod_fazenda), {})
        nome_fazenda = fazenda_info.get('FUNDO AGRICOLA', "")
        almox = fazenda_info.get('ALMOX', "")
        filial = fazenda_info.get('FILIAL', "")
        # Preenche os campos nome_fazenda_entry e filial_entry
        self.nome_fazenda_entry.delete(0, END)
        self.nome_fazenda_entry.insert(0, nome_fazenda)

        self.almox_entry.delete(0, END)
        self.almox_entry.insert(0, almox)

        self.filial_entry.delete(0, END)
        self.filial_entry.insert(0, filial)
    def carregar_dados_responsavel(self):
        dados = pd.read_excel('C:/Users/Eliom/OneDrive/Área de Trabalho/APLICATIVO/DADOS CADASTRAIS.xlsx', sheet_name="FUNCIONARIOS")

        self.dados_fun = {}
        for index, row in dados.iterrows():
            cod_responsavel = row['Codigo']
            nome_reponsavel = row['Nome']
            self.dados_fun[int(cod_responsavel)] = {'Nome': nome_reponsavel}
    def preencher_nome_responsavel(self, *args):
        #Obtém o valor do campo cod_fazenda_entry      
        cod_responsavel = self.cod_responsavel_entry.get()       
        # Obtém o nome da fazenda e a filial com base no código
        responsavel_info = self.dados_fun.get(int(cod_responsavel), {})
        nome_responsavel = responsavel_info.get('Nome', "")

        # Preenche os campos nome_fazenda_entry e filial_entry
        self.nome_responsavel_entry.delete(0, END)
        self.nome_responsavel_entry.insert(0, nome_responsavel)
    def carregar_dados_produtos(self):
        dados = pd.read_excel('C:/Users/Eliom/OneDrive/Área de Trabalho/APLICATIVO/DADOS CADASTRAIS.xlsx', sheet_name="PRODUTOS")

        self.dados_product = {}
        for index, row in dados.iterrows():
            cod_produto = row['Codigo']
            nome_produto = row['Descricao']
            unidade = row['Unidade']
            self.dados_product[int(cod_produto)] = {'Descricao': nome_produto, 'Unidade': unidade}
    def preencher_produtos(self, *args):
        cod_produto = self.cod_produto_1.get()       
        # Obtém o nome da fazenda e a filial com base no código
        produto_info = self.dados_product.get(int(cod_produto), {})
        nome_produto = produto_info.get('Descricao', "")
        unidade = produto_info.get('Unidade', "")
        # Preenche os campos nome_fazenda_entry e filial_entry
        self.nome_produto_entry.delete(0, END)
        self.nome_produto_entry.insert(0, nome_produto)

        self.unidade_entry_1.delete(0, END)
        self.unidade_entry_1.insert(0, unidade)
    def preencher_data(self):
        # Obtém a data atual no formato "dia/mês/ano"
        data_atual = datetime.now().strftime("%d/%m/%Y")

        # Preenche o campo data_entry com a data atual
        self.data_entry.delete(0, END)
        self.data_entry.insert(0, data_atual)


    def Menu(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        menubar.add_cascade(label="RELATÓRIOS", menu=filemenu)
        filemenu.add_command(label="SAIDA X DEVOLUÇÃO", command=self.abrir_pesquisa)
        # Remova a linha abaixo
        # filemenu.add_command(label="Sair", command=self.janela.quit)

    def abrir_pesquisa(self):
            # Cria uma nova janela para a pesquisa
            pesquisa_window = Toplevel(self.janela)
            pesquisa_window.title("Pesquisar Requisições")
            pesquisa_window.geometry("200x100")

            # Cria os widgets para a entrada da OS
            label_os = Label(pesquisa_window, text="Número da OS:")
            label_os.grid(row=0, column=0, padx=10, pady=10)
            entry_os = Entry(pesquisa_window)
            entry_os.grid(row=0, column=1, padx=5, pady=5)

            # Função para executar a pesquisa
            def pesquisar():
                os_pesquisada = entry_os.get()  # Obtém a OS digitada

                # Chama o método para gerar o relatório PDF com base na OS fornecida
                self.gerar_relatorio_pdf(os_pesquisada)

            # Cria o botão de pesquisa
            button_pesquisar = Button(pesquisa_window, text="Pesquisar", command=pesquisar)
            button_pesquisar.grid(row=1, column=0, columnspan=2, pady=10)


Application()