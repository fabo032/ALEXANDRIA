#Aluno- Fábio Nascimento Rodrigues Turma: 1D
#Professor (a): Luiz Carlos dos Santos Filho 
#08/06/2024- Software Basico
#Pré-Projeto CRUD com SQL: Controle de estoque de Livraria 

import os
import locale
import sqlite3
from contextlib import closing

# Configuraçao de localidade para formataçao de moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


# Cor para texto e fundo/ Estilo 
cor_vermelha = '\033[91m'
cor_verde = '\033[92m'
cor_amarela = '\033[93m'
cor_azul = '\033[94m'
cor_roxa = '\033[95m'
cor_ciano = '\033[96m'
cor_branca = '\033[97m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_roxo = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'
estilo_negrito = '\033[1m'
estilo_sublinhado = '\033[4m'
resetar_estilo = '\033[0m'

# Conectar-se ao banco de dados (criará um novo se não existir) 
mangas = sqlite3.connect('mangas.db')
cursor = mangas.cursor()

# Salvar as mudanças e fechar a conexão
mangas.commit()
mangas.close()

# Dicionario.db de livros com etiqueta, nome, estoque e preço
def dados():
    mangas = sqlite3.connect('mangas.db')
    cursor = mangas.cursor()
    cursor.execute('SELECT * FROM mangas')
    data = cursor.fetchall()
    mangas.close()

    # Formatando os dados
    result = {}
    for linha in data:
        etiqueta, nome, estoque, preco = linha
        result[str(etiqueta)] = [nome, estoque, preco]
    return result
DD=dados()

# Função para exibir o relatório dos livros
def relatorio():
    mangas = sqlite3.connect('mangas.db')
    cursor = mangas.cursor()

    # Selecionar todos os registros da tabela mangas
    cursor.execute('SELECT * FROM mangas')
    linhas = cursor.fetchall()

    # Imprimir o cabeçalho
    print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)

    # Imprimir cada registro formatado
    for linha in linhas:
        etiqueta, nome, estoque, preco = linha
        preco_formatado = locale.currency(float(preco), grouping=True, symbol=True)
        print(cor_ciano + fundo_branco + f'{etiqueta:<10} {nome:<15} {estoque:^8} {preco_formatado:^10}' + resetar_estilo)

    # Fechar a conexão com o banco de dados
    mangas.close()
    
# Função para adicionar um novo livro
def inclusao():
    while True:
        os.system('cls')

        # Verificação de número inteiro
        while True:
            etiqueta = input(cor_azul + estilo_negrito + "Entre com a nova etiqueta do livro (somente números): ")
            if etiqueta.isdigit():
                break
            else:
                os.system('cls')
                print(cor_azul + estilo_negrito + "Erro: A etiqueta deve conter apenas número inteiro. Tente novamente.")
                 
        if etiqueta in DD:
            print(cor_azul + estilo_negrito + "Etiqueta já existente na Base")
        else:
            nome = input(cor_azul + estilo_negrito + "Entre com o nome: ")
            
            # Verificação de número inteiro
            while True:
                estoque = input(cor_azul + estilo_negrito + "Entre com o estoque: ")
                if estoque.isdigit():
                    break
                else:
                    print(cor_azul + estilo_negrito + "Erro: O estoque deve conter apenas números inteiro. Tente novamente.")
            
            # Verificação de número real
            while True:
                preco = input(cor_azul + estilo_negrito + "Entre com o preço: ")
                if preco.replace('.', '', 1).isdigit():
                    break
                else:
                    print(cor_azul + estilo_negrito + "Erro: O preço deve ser um número real. Tente novamente.")
            
            DD[etiqueta] = [nome, str(estoque), str(preco)]  # Adiciona o novo livro ao dicionário DD
            

            # Livro novo add
            print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
            info = DD[etiqueta]
            preco_formatado = locale.currency(float(info[2]), grouping=True, symbol=True)
            print(cor_ciano + fundo_branco + f'{etiqueta:<10} {info[0]:<15} {info[1]:^8} {preco_formatado:^10}' + resetar_estilo)
            print(cor_azul + estilo_negrito + 'Registro Adicionado')
        
            with sqlite3.connect("mangas.db") as conexão:
                with closing(conexão.cursor()) as cursor:
                    cursor.execute("INSERT INTO mangas (etiqueta, nome, estoque, preço) VALUES (?, ?, ?, ?)", (etiqueta, nome, estoque, preco))
                    conexão.commit()

        # Add mais livros
        add_mais = input(cor_azul + estilo_negrito + "Deseja adicionar mais um livro? (s/n): ").lower()
        if add_mais != 's':
            break

# Funçao para remover um livro existente
def remocao():
    while True:
        os.system('cls')
        # Verificação de número inteiro
        while True:
            etiqueta = input(cor_vermelha + estilo_negrito + "Entre com a etiqueta do livro a ser removido (somente números): ")
            if etiqueta.isdigit():
                break
            else:
                os.system('cls')
                print(cor_vermelha + estilo_negrito + "Erro: A etiqueta deve conter apenas número inteiro. Tente novamente.")
        # Livro pesquisado         
        print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
        info = DD[etiqueta]
        preco_formatado = locale.currency(float(info[2]), grouping=True, symbol=True)
        print(cor_ciano + fundo_branco + f'{etiqueta:<10} {info[0]:<15} {info[1]:^8} {preco_formatado:^10}' + resetar_estilo)

        if etiqueta in DD:
            confirmacao = input(cor_vermelha + estilo_negrito + f"Tem certeza que deseja remover o livro '{DD[etiqueta][0]}'? (s/n): ")
            if confirmacao.lower() == "s": #lower() serve para deixar as letra todas no minusculo 
                del DD[etiqueta]
                
                print(cor_vermelha + estilo_negrito + "Livro removido com sucesso")
                with sqlite3.connect("mangas.db") as conexão:
                    with closing(conexão.cursor()) as cursor:
                        cursor.execute("DELETE FROM mangas WHERE etiqueta=?", (etiqueta,))
                        conexão.commit()

            elif confirmacao.lower() == "nao":
                print(cor_vermelha + estilo_negrito + "Operaçao de remoçao cancelada.")
            else:
                print(cor_vermelha + estilo_negrito + "Opçao invalida.")

            # Rmv mais livros
            rmv_mais = input(cor_vermelha + estilo_negrito + "Deseja remover mais um livro? (s/n): ").lower()
            if rmv_mais != 's':
                break
        else:
            print(cor_vermelha + estilo_negrito + "Livro nao encontrado")

# Funçao para alterar informaçoes de um livro
def alteracao():
    os.system('cls')

    # Verificação de número inteiro
    while True:
        etiqueta = input(cor_verde + estilo_negrito + "Entre com a etiqueta do livro a ser alterado (somente números): " + resetar_estilo)
        if etiqueta.isdigit():
            break
        else:
            os.system('cls')
            print(cor_verde + estilo_negrito +"Erro: A etiqueta deve conter apenas número inteiro. Tente novamente.")
    
    # Conectar ao banco de dados
    with sqlite3.connect("mangas.db") as mangas:
        cursor = mangas.cursor()

        # Consulta SQL para verificar se a etiqueta existe 
        cursor.execute("SELECT * FROM mangas WHERE etiqueta = ?", (etiqueta,))
        linha = cursor.fetchone()

        # Livro encontrado
        if linha:
            etiqueta, nome, estoque, preco = linha
            preco_formatado = locale.currency(float(preco), grouping=True, symbol=True)
            print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
            print(cor_ciano + fundo_branco + f'{etiqueta:<10} {nome:<15} {estoque:^8} {preco_formatado:^10}' + resetar_estilo)
            
            while True:
                print(cor_verde + estilo_negrito + f"O que você deseja alterar para o livro '{nome}'?" + resetar_estilo)
                print(estilo_negrito + '''
            Escolha uma opção:
            [1] Nome
            [2] Estoque
            [3] Preço
            [4] Sair
            ''' + resetar_estilo)
                opcao = input(estilo_negrito +"Opção: ")
                
                if opcao == "1":
                    os.system('cls')
                    novo_nome = input(cor_verde + estilo_negrito + "Novo nome: ")
                    cursor.execute("UPDATE mangas SET nome = ? WHERE etiqueta = ?", (novo_nome, etiqueta))
                    mangas.commit()
                    print(cor_verde + estilo_negrito + "Nome alterado com sucesso.")

                elif opcao == "2":
                    os.system('cls')
                    while True:
                        novo_estoque = input(cor_verde + estilo_negrito + "Novo estoque: ")
                        if novo_estoque.isdigit():
                            cursor.execute("UPDATE mangas SET estoque = ? WHERE etiqueta = ?", (novo_estoque, etiqueta))
                            mangas.commit()
                            print(cor_verde + estilo_negrito + "Estoque alterado com sucesso.")
                            break
                        else:
                            print(cor_verde + estilo_negrito + "Erro: O estoque deve conter apenas números inteiros. Tente novamente.")

                elif opcao == "3":
                    os.system('cls')
                    while True:
                        novo_preco = input(cor_verde + estilo_negrito + "Novo preço: ")
                        if novo_preco.replace('.', '', 1).isdigit():  # Verifica se é um número real válido
                            cursor.execute("UPDATE mangas SET preço = ? WHERE etiqueta = ?", (novo_preco, etiqueta))
                            mangas.commit()
                            print(cor_verde + estilo_negrito + "Preço alterado com sucesso.")
                            break
                        else:
                            print(cor_verde + estilo_negrito + "Erro: O preço deve conter apenas números reais. Tente novamente.")
                            
                elif opcao == "4":
                    os.system('cls')
                    break
                else:
                    print(cor_verde + estilo_negrito + "Opção inválida.")
                
                # Alterar mais alguma coisa
                alt_mais = input(cor_verde + estilo_negrito + "Deseja alterar mais alguma coisa? (s/n): ").lower()
                if alt_mais != 's':
                    break
        else:
            print(cor_verde + estilo_negrito + "Livro não encontrado.")
    
# Loop principal do programa 
while True:
    os.system('cls')
    print(cor_roxa + ''' 
   ▄████████  ▄█          ▄████████ ▀████    ▐████▀    ▄████████ ███▄▄▄▄   ████████▄     ▄████████  ▄█     ▄████████ 
  ███    ███ ███         ███    ███   ███▌   ████▀    ███    ███ ███▀▀▀██▄ ███   ▀███   ███    ███ ███    ███    ███ 
  ███    ███ ███         ███    █▀     ███  ▐███      ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    ███ 
  ███    ███ ███        ▄███▄▄▄        ▀███▄███▀      ███    ███ ███   ███ ███    ███  ▄███▄▄▄▄██▀ ███▌   ███    ███ 
▀███████████ ███       ▀▀███▀▀▀        ████▀██▄     ▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀███████████ 
  ███    ███ ███         ███    █▄    ▐███  ▀███      ███    ███ ███   ███ ███    ███ ▀███████████ ███    ███    ███ 
  ███    ███ ███▌    ▄   ███    ███  ▄███     ███▄    ███    ███ ███   ███ ███   ▄███   ███    ███ ███    ███    ███ 
  ███    █▀  █████▄▄██   ██████████ ████       ███▄   ███    █▀   ▀█   █▀  ████████▀    ███    ███ █▀     ███    █▀  
             ▀                                                                          ███    ███                   
 ''' + resetar_estilo)
    print(estilo_negrito + '''
    Escolha uma opçao:
    [1] Pesquisa por livro
    [2] Relatorio do estoque
    [3] Inclusao livro
    [4] Remoçao livro
    [5] Alteraçao livro
    [6] Sair
    ''' + resetar_estilo)
    opt = input("Opçao = ")

    if opt not in ["1","2","3","4","5","6"]:
     os.system('cls')
     print ("Opção inválida.")
     input ("Enter para voltar ao Menu")
     
    if opt == "1":
        os.system('cls')
        mangas = sqlite3.connect("mangas.db")
        cursor = mangas.cursor()
        print(cor_amarela + estilo_negrito + "Escolha o método de pesquisa:")
        print('''
        [1] Por Nome 
        [2] Por Etiqueta 
        ''')
        opt1 = input(cor_amarela + estilo_negrito +"Opção: ")

        if opt1 == "1":
            os.system('cls')
            nome_pesquisa = input(cor_amarela + estilo_negrito +"Digite o nome do livro a pesquisar: ").lower()
            cursor.execute("SELECT * FROM mangas WHERE nome LIKE ?", ('%' + nome_pesquisa + '%',))
            linhas = cursor.fetchall()
            print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
            for linha in linhas:
                etiqueta, nome, estoque, preco = linha
                preco_formatado = locale.currency(float(preco), grouping=True, symbol=True)
                print(cor_ciano + fundo_branco + f'{etiqueta:<10} {nome:<15} {estoque:^8} {preco_formatado:^10}' + resetar_estilo)
            input(cor_amarela + estilo_negrito +"Enter para voltar ao Menu")

        elif opt1 == "2":
            os.system('cls')
            while True:
                etiqueta = input(cor_amarela + estilo_negrito +"Entre com a etiqueta do livro a pesquisar (somente números): ")
                if etiqueta.isdigit():
                    cursor.execute("SELECT * FROM mangas WHERE etiqueta = ?", (etiqueta,))
                    linha = cursor.fetchone()
                    print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
                    if linha:
                        etiqueta, nome, estoque, preco = linha
                        preco_formatado = locale.currency(float(preco), grouping=True, symbol=True)
                        print(cor_ciano + fundo_branco + f'{etiqueta:<10} {nome:<15} {estoque:^8} {preco_formatado:^10}' + resetar_estilo)
                    else:
                        print(cor_amarela + estilo_negrito +"Etiqueta não encontrada.")
                    break
                else:
                    os.system('cls')
                    print(cor_amarela + estilo_negrito +"Erro: A etiqueta deve conter apenas número inteiro. Tente novamente.")
            input(cor_amarela + estilo_negrito +"Enter para voltar ao Menu")

        else:
            print(cor_amarela + estilo_negrito +"Opção inválida.")
            input(cor_amarela + estilo_negrito +"Enter para voltar ao Menu")

        mangas.close()    
    elif opt == "2":
        relatorio()
        input(cor_ciano + estilo_negrito +"Enter para voltar ao Menu")
    elif opt == "3":
        inclusao()
        input(cor_azul + estilo_negrito +"Enter para voltar ao Menu")
    elif opt == "4":
        remocao()
        input(cor_vermelha + estilo_negrito +"Enter para voltar ao Menu")
    elif opt == "5":
        alteracao()
        input(cor_verde + estilo_negrito +"Enter para voltar ao Menu")
    elif opt == "6":
        os.system('cls')
        print(estilo_negrito + '''
        ███████╗██╗███╗   ███╗    ██████╗  ██████╗     ██████╗ ██████╗  ██████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗ █████╗ 
        ██╔════╝██║████╗ ████║    ██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔══██╗
        █████╗  ██║██╔████╔██║    ██║  ██║██║   ██║    ██████╔╝██████╔╝██║   ██║██║  ███╗██████╔╝███████║██╔████╔██║███████║
        ██╔══╝  ██║██║╚██╔╝██║    ██║  ██║██║   ██║    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██╔══██║
        ██║     ██║██║ ╚═╝ ██║    ██████╔╝╚██████╔╝    ██║     ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║
        ╚═╝     ╚═╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
        ''')
        break