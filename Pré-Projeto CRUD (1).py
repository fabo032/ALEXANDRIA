#Aluno- Fábio Nascimento Rodrigues Turma: 1D
#Professor (a): Luiz Carlos dos Santos Filho 
#30/04/2024- Software Basico
#Pré-Projeto CRUD: Controle de estoque de Livraria 

import os
import locale

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

# Dicionario de livros com etiqueta, nome, estoque e preço
livros = {
    1: ["death note", 10, 36.90],
    2: ["harry poter", 5, 50.90],
    3: ["Acaso", 12, 30.00],
    4: ["Vagabound", 1, 40.90],
    5: ["Gyo", 8, 69.90]
}

# Funçao para exibir o relatorio dos livros
def relatorio():
    os.system('cls')
    print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
    for etiqueta, info in livros.items():
        preco_formatado = locale.currency(info[2], grouping=True, symbol=True)
        print(cor_ciano + fundo_branco + f'{etiqueta:<10} {info[0]:<15} {info[1]:^8} {preco_formatado:^10}' + resetar_estilo)

# Funçao para adicionar um novo livro
def inclusao():
    os.system('cls')
    etiqueta = int(input(cor_azul + estilo_negrito + "Entre com a etiqueta do livro: "))
    if etiqueta not in livros:
        nome = input("Entre com o nome: ")
        estoque =int(input("Entre com o estoque: "))
        preco = float(input("Entre com o preço: "))
        livros[etiqueta] = [nome, estoque, preco]
        print ('Registro Adicionado')
    else:
        print ("Etiqueta ja existente na Base")

# Funçao para remover um livro existente
def remocao():
    os.system('cls')
    etiqueta = int(input(cor_vermelha + estilo_negrito + "Entre com a etiqueta do livro a ser removido: "))
    if etiqueta in livros:
        confirmacao = input(f"Tem certeza que deseja remover o livro '{livros[etiqueta][0]}'? (sim/nao): ")
        if confirmacao.lower() == "sim": #lower() serve para deixar as letra todas no minusculo 
            del livros[etiqueta]
            print("Livro removido com sucesso")
        elif confirmacao.lower() == "nao":
            print("Operaçao de remoçao cancelada.")
        else:
            print("Opçao invalida.")
    else:
        print("Livro nao encontrado")

# Funçao para alterar informaçoes de um livro
def alteracao():
    os.system('cls')
    etiqueta = int(input(cor_verde + estilo_negrito + "Entre com a etiqueta do livro a ser alterado: "))
    if etiqueta in livros:
        print(f"O que voce deseja alterar para o livro '{livros[etiqueta][0]}'?")
        print(estilo_negrito +'''
    Escolha uma opçao:
    [1] Nome
    [2] Estoque
    [3] Preço
    ''')
        opcao = input("Opçao: ")
        if opcao == "1":
            novo_nome = input("Novo nome: ")
            livros[etiqueta][0] = novo_nome
            print("Nome alterado com sucesso.")
        elif opcao == "2":
            novo_estoque = int(input("Novo estoque: "))
            livros[etiqueta][1] = novo_estoque
            print("Estoque alterado com sucesso.")
        elif opcao == "3":
            novo_preco = float(input("Novo preço: "))
            livros[etiqueta][2] = novo_preco
            print("Preço alterado com sucesso.")
        else:
            print("Opçao invalida.")
    else:
        print("Livro nao encontrado")

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
        print(cor_amarela + estilo_negrito + "Escolha o método de pesquisa:")
        print('''
        [1] Por Nome 
        [2] Por Etiqueta 
        ''')
        opt1 = input("Opção: ")
        if opt1 == "1":
            os.system('cls')
            nome_pesquisa = input("Digite o nome do livro a pesquisar: ").lower()
            print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
            for etiqueta, info in livros.items():
             if nome_pesquisa in info[0].lower():
                preco_formatado = locale.currency(info[2], grouping=True, symbol=True)
                print(cor_ciano + fundo_branco + f'{etiqueta:<10} {info[0]:<15} {info[1]:^8} {preco_formatado:^10}' + resetar_estilo)
            input("Enter para voltar ao Menu")
        elif opt1 == "2":
            os.system('cls')
            etiqueta = int(input("Entre com a etiqueta do livro a pesquisar: "))
            print(fundo_ciano + "Etiqueta   Nome           Estoque   Preço" + resetar_estilo)
            if etiqueta in livros:
                info = livros[etiqueta]
                preco_formatado = locale.currency(info[2], grouping=True, symbol=True)
                print(cor_ciano + fundo_branco + f'{etiqueta:<10} {info[0]:<15} {info[1]:^8} {preco_formatado:^10}' + resetar_estilo)
            input("Enter para voltar ao Menu")
        else:
            print("Opção inválida.")
            input("Enter para voltar ao Menu")    
    elif opt == "2":
        relatorio()
        input("Enter para voltar ao Menu")

    elif opt == "3":
        inclusao()
        input('Enter para voltar ao Menu')

    elif opt == "4":
        remocao()
        input("Enter para voltar ao Menu")

    elif opt == "5":
        alteracao()
        input("Enter para voltar ao Menu")

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