#Aluno- Fábio Nascimento Rodrigues Turma: 1D
#Professor (a): Luiz Carlos dos Santos Filho 
#08/06/2024- Software Basico
#Projeto Alexandria-CRUD com SQL/TKK: Controle de estoque de Livraria

#######################################################################################################################
#   ▄████████  ▄█          ▄████████ ▀████    ▐████▀    ▄████████ ███▄▄▄▄   ████████▄     ▄████████  ▄█     ▄████████ # 
#  ███    ███ ███         ███    ███   ███▌   ████▀    ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███ ███    ███    ███ #
#  ███    ███ ███         ███    █▀     ███  ▐███      ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    ███ #
#  ███    ███ ███        ▄███▄▄▄        ▀███▄███▀      ███    ███ ███   ███ ███    ███  ▄███▄▄▄▄██▀ ███▌   ███    ███ #
#▀███████████ ███       ▀▀███▀▀▀        ████▀██▄     ▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀███████████ #
#  ███    ███ ███         ███    █▄    ▐███  ▀███      ███    ███ ███   ███ ███    ███ ▀███████████ ███    ███    ███ #
#  ███    ███ ███▌    ▄   ███    ███  ▄███     ███▄    ███    ███ ███   ███ ███   ▄███   ███    ███ ███    ███    ███ #
#  ███    █▀  █████▄▄██   ██████████ ████       ███▄   ███    █▀   ▀█   █▀  ████████▀    ███    ███ █▀     ███    █▀  #
#             ▀                                                                                                       #
#######################################################################################################################

# Bibliotecas:
import sqlite3
from contextlib import closing
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
from PIL import Image, ImageTk

# Instancia a classe TK:
Janela = Tk()

# Título e tamanho da janela:
Janela.title("Controle de estoque de Livraria")
Janela.geometry('800x600')

# Label com instruções:
Tit = Label(Janela, text="Selecione uma das opções abaixo:")
Tit.place(x=0, y=0)
Tit["font"] = ("Code", "12", "italic", "bold")
Tit["fg"] = "purple"
Tit["bg"] = "white"

# Função Selecionar:
def Selecionar():
    tree.delete(*tree.get_children())  # Apaga registros da Treeview
    tree.place(x=220, y=25)
    label_nova_etiqueta.place_forget()
    label_novo_nome.place_forget()
    label_novo_estoque.place_forget()
    label_novo_preço.place_forget()
    label_info.place_forget()
    Botao_Alterar.place_forget()
    etiqueta_entry.place_forget()
    nome_entry.place_forget()
    estoque_entry.place_forget()
    preco_entry.place_forget()
    Botao_Save.place_forget()
    Botao_Retornar.place_forget()
    Botao_Exc['state'] = NORMAL
    Botao_Inc['state'] = NORMAL
    Botao_Alt['state'] = NORMAL
    # Acesso Banco
    with sqlite3.connect("mangas.db") as conexão:
        with closing(conexão.cursor()) as cursor:
            cursor.execute('SELECT * FROM mangas')
            resultado = cursor.fetchall()
            for i in resultado:
                tree.insert('', END, values=i)

# Função de Inclusão:
def Inc():  
    etiqueta_entry.delete(0, END)  # apaga dados da caixa Entry
    nome_entry.delete(0, END)
    estoque_entry.delete(0, END)
    preco_entry.delete(0, END)
    tree.place_forget()  # esconde widget da tela anterior
    label_info_moise.place_forget()
    label_info_alt_exc.place_forget()
    label_pesquisa_etiqueta.place_forget()
    pesquisa_etiqueta_entry.place_forget()
    label_pesquisa_nome.place_forget()
    pesquisa_nome_entry.place_forget()
    Botao_Pesquisar.place_forget()
    Botao_Exc['state'] = DISABLED  # desabilita botões desnecessários no modo inclusão
    Botao_Alt['state'] = DISABLED
    label_nova_etiqueta.place(x=220, y=25)  # posiciona widgets de inclusão
    etiqueta_entry.place(x=400, y=25)
    label_novo_nome.place(x=220, y=50)
    nome_entry.place(x=400, y=50)
    label_novo_estoque.place(x=220, y=75)
    estoque_entry.place(x=400, y=75)
    label_novo_preço.place(x=220, y=100)
    preco_entry.place(x=400, y=100)
    Botao_Save.place(x=220, y=130)
    Botao_Retornar.place(x=450, y=130)

# Validação para permitir apenas números
def validate_number_input(action, value_if_allowed):
    if action == '1': 
        return value_if_allowed.isdigit()
    return True

# salva no banco dados digitados
def Salvar():
    etiqueta = etiqueta_entry.get()
    nome = nome_entry.get()
    estoque = estoque_entry.get()
    preco = preco_entry.get()
    try:
        with sqlite3.connect("mangas.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute("INSERT INTO mangas (etiqueta, nome, estoque, preço) VALUES (?, ?, ?, ?)", (etiqueta, nome, estoque, preco))
                conexão.commit()
            showinfo(title='Atenção', message='Registro Incluído')
    except sqlite3.IntegrityError:  # verificando se registro já existe no banco
        showinfo(title='Atenção', message='Registro Já Existente')

# Função de Exclusão:
def Exc():
    Botao_Inc['state'] = DISABLED 
    Botao_Alt['state'] = DISABLED
    # verifica se existe registro selecionado na Tree View
    if not tree.focus():  
        showinfo(title='ERRO', message='Selecione um item para Exclusão')
        Selecionar()  
    else:
        # Coletando qual item está selecionado.
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        etiqueta_Exc = rowid["values"][0]
        answer = askyesno(title='Confirmação', message='Tem certeza de que deseja excluir o item selecionado?')
        if answer:
            with sqlite3.connect("mangas.db") as conexão:
                with closing(conexão.cursor()) as cursor:
                    cursor.execute("DELETE FROM mangas WHERE etiqueta = ?", (etiqueta_Exc,))
                    conexão.commit()
                    tree.delete(item_selecionado)
                    showinfo(title='Sucesso', message='Item excluído com sucesso')
            Selecionar()  
        else:
            showinfo(title='Cancelado', message='Operação de exclusão cancelada')
            Selecionar()

# Função de Alterasão:
def Alt():
    Botao_Exc['state'] = DISABLED
    Botao_Inc['state'] = DISABLED
    global etiqueta_Alt
    global nome_Alt
    global estoque_Alt
    global preco_Alt

    nome_entry.delete(0, END)
    estoque_entry.delete(0, END)
    preco_entry.delete(0, END)
    etiqueta_entry.delete(0, END)
    
    if not tree.focus():
        showinfo(title='ERRO', message='Selecione um item para Alteração')
        Selecionar()
    else:
        # esconde mensagens de rolagem de página e seleção de itens
        label_info_moise.place_forget()
        label_info_alt_exc.place_forget()
        # Coletando qual item está selecionado.
        item_selecionado = tree.focus()
        rowid = tree.item(item_selecionado)
        etiqueta_Alt = rowid["values"][0]
        nome_Alt = rowid["values"][1]
        estoque_Alt = rowid["values"][2]
        preco_Alt = rowid["values"][3]
        # prepara tela e coloca informações para alteração
        label_info.place(x=180, y=250)
        etiqueta_entry.insert(0, etiqueta_Alt)
        nome_entry.insert(0, nome_Alt)
        estoque_entry.insert(0, estoque_Alt)
        preco_entry.insert(0, preco_Alt)
        nome_entry.place(x=180, y=275)
        estoque_entry.place(x=180, y=300)
        preco_entry.place(x=180, y=325)
        Botao_Alterar.place(x=180, y=350) # botões de alterar e retornar
        Botao_Retornar.place(x=180, y=375)

def Alterar():
    global etiqueta_Alt
    nome_Alt = nome_entry.get()
    estoque_Alt = estoque_entry.get()
    preco_Alt = preco_entry.get()
    
    try:
        with sqlite3.connect("mangas.db") as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute('UPDATE mangas SET nome = ?, estoque = ?, preço = ? WHERE etiqueta = ?', (nome_Alt, estoque_Alt, preco_Alt, etiqueta_Alt))
                conexão.commit()            
        selected_item = tree.selection()[0]
        tree.item(selected_item, values=(etiqueta_Alt, nome_Alt, estoque_Alt, preco_Alt))
        showinfo(title='Atenção', message='Registro Alterado')
        Selecionar()
    except sqlite3.Error as e:
        showinfo(title='Erro', message=f'Ocorreu um erro ao tentar alterar o registro: {e}')

def Pesquisar(etiqueta, nome):
    query = "SELECT * FROM mangas WHERE 1=1"
    params = []

    if etiqueta:
        query += " AND etiqueta LIKE ?"
        params.append(f"%{etiqueta}%")

    if nome:
        query += " AND nome LIKE ?"
        params.append(f"%{nome}%")

    tree.delete(*tree.get_children())  # Limpa registros da Treeview

    with sqlite3.connect("mangas.db") as conexão:
        with closing(conexão.cursor()) as cursor:
            cursor.execute(query, params)
            resultado = cursor.fetchall()
            for i in resultado:
                tree.insert('', END, values=i)

    showinfo(title='Atenção', message=f'{len(resultado)} registro(s) encontrado(s)')

#1- Botão Selecionar:
Botao_Sel = Button(Janela, text="Relatório de Estoque", width=30, command=Selecionar)
Botao_Sel.place(x=0, y=25)

#2- Botão Inclusão:
Botao_Inc = Button(Janela, text="Incluir livros", width=30, command=Inc)
Botao_Inc.place(x=0, y=50)

# Cria caixas e labels para entrada de dados
vcmd = (Janela.register(validate_number_input), '%d', '%P')  # '%d' is the type of action (1 for insert, 0 for delete, etc.), and '%P' is the value of the entry if the edit is allowed

label_nova_etiqueta = Label(Janela, text="Entre com a etiqueta do livro")
etiqueta_entry = Entry(Janela, width=10, validate='key', validatecommand=vcmd)
label_novo_nome = Label(Janela, text="Entre com o nome do livro")
nome_entry = Entry(Janela, width=30)
label_novo_estoque = Label(Janela, text="Entre com o estoque do livro")
estoque_entry = Entry(Janela, width=50, validate='key', validatecommand=vcmd)
label_novo_preço = Label(Janela, text="Entre com o preço do livro")
preco_entry = Entry(Janela, width=70, validate='key', validatecommand=vcmd)

Botao_Save = Button(Janela, text="Incluir Livro", width=30, command=Salvar)
Botao_Retornar = Button(Janela, text="Retornar", width=30, command=Selecionar)

#3- Botão Excluir:
Botao_Exc = Button(Janela, text="Excluir Livros", width=30)
Botao_Exc.place(x=0, y=75)
Botao_Exc['command']=Exc

#4- Botão Alterar:
Botao_Alt = Button(Janela, text="Alterar Informações", width=30)
Botao_Alt.place(x=0, y=100)
label_info = Label (Janela, text = "Entre com as novas informações ")
Botao_Alt['command']=Alt
Botao_Alterar = Button(Janela, text="Salvar Alterações",width=30)
Botao_Alterar['command']=Alterar

#5- Botão Sair:
Sair = Button(Janela, text="Sair da Aplicação", command=Janela.destroy, width=30)
Sair.place(x=0, y=125)

#6 Botão de pesquisa:
Botao_Pesquisar = Button(Janela, text="Pesquisar", width=30, command=lambda: Pesquisar(pesquisa_etiqueta_entry.get(), pesquisa_nome_entry.get()))
Botao_Pesquisar.place(x=0, y=350)

# Labels e entradas para pesquisa
label_pesquisa_etiqueta = Label(Janela, text="Pesquisar por etiqueta")
label_pesquisa_etiqueta.place(x=0, y=300)
pesquisa_etiqueta_entry = Entry(Janela, width=30,  validate='key', validatecommand=vcmd)
pesquisa_etiqueta_entry.place(x=150, y=300)

label_pesquisa_nome = Label(Janela, text="Pesquisar por nome")
label_pesquisa_nome.place(x=0, y=325)
pesquisa_nome_entry = Entry(Janela, width=30)
pesquisa_nome_entry.place(x=150, y=325)

# TreeView - define columns Treeview
columns = ('Etiqueta', 'nome', 'Estoque', 'Preço')
tree = ttk.Treeview(Janela, columns=columns, show='headings')

# define headings
tree.column('#1', width=125)
tree.column('#2', width=150)
tree.column('#3', width=125)
tree.column('#4', width=150)
tree.heading('Etiqueta', text='Etiqueta do Livro')
tree.heading('nome', text='nome do Livro')
tree.heading('Estoque', text='Estoque do Livro')
tree.heading('Preço', text='Preço do Livro')

# Exibe a TreeView
label_info_moise = Label(Janela, text="Role a tela para baixo com o Mouse")
label_info_moise.place(x=220, y=260)
label_info_moise["font"] = ("Code", "8", "bold")
label_info_moise["fg"] = "blue"
label_info_moise["bg"] = "white"

label_info_alt_exc = Label(Janela, text="Selecione o registro para Alterar/Excluir")
label_info_alt_exc.place(x=220, y=280)
label_info_alt_exc["font"] = ("Code", "8", "bold")
label_info_alt_exc["fg"] = "red"
label_info_alt_exc["bg"] = "white"

# Chama a função Selecionar para carregar os dados inicialmente
Selecionar()

# Logo:
image = Image.open("Alexandria Logo.bmp")
resize_image = image.resize((200, 200))
img = ImageTk.PhotoImage(resize_image)
Logo = Label(Janela, image=img)
Logo.image = img
Logo.place(x=600, y=400)

# Fim do Loop:
Janela.mainloop()
