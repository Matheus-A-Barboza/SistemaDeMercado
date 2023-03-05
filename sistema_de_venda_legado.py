from time import sleep

# Funcoes
def load():
    sleep(5)

def shortLoad():
    sleep(2)


# Listas
alimentos = ["ARROZ", "FEIJAO", "MACARRAO", "CARNE"]
produtosDeLimpeza = ["AGUA SANITARIA", "DESINFETANTE", "DETERGENTE"]
higiene = ["PAPEL HIGIENICO", "ESCOVA DE DENTES", "SABONETE EM BARRA"]

# Codigo

nomeUser = input("Olá, Usuário. Qual seu nome?\n")
shortLoad()

while True:
    escolhaMenu = input(
        f'Olá, {nomeUser}. O que você gostaria de fazer?\n1- Consultar Produtos\n2- Cadastrar Produtos\n3- Ver Deposito\n4- Excluir Produto\n')
    shortLoad()

    # Configurando a Consulta
    if escolhaMenu == "1":
        while True:
            escolhaConsulta = input(
                f'{nomeUser}, o que gostaria de Consultar?\n1- Alimentos\n2- Produtos de Limpeza\n3- Produtos de Higiene\n')
            if escolhaConsulta == "1":
                load()
                print(alimentos)
                shortLoad()
                continuarConsulta = input("1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n")
                if continuarConsulta == "1":
                    load()
                elif continuarConsulta == "2":
                    shortLoad()
                    break
                elif continuarConsulta == "3":
                    exit()
                else:
                    print("Este comando é inválido. Retornando para Menu Principal.")
                    load()
                    continue

            elif escolhaConsulta == "2":
                load()
                print(produtosDeLimpeza)
                shortLoad()
                continuarConsulta = input("1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n")
                if continuarConsulta == "1":
                    load()
                elif continuarConsulta == "2":
                    shortLoad()
                    break
                elif continuarConsulta == "3":
                    exit()
                else:
                    print("Este comando é inválido. Retornando para Menu Principal.")
                    load()
                    continue

            elif escolhaConsulta == "3":
                load()
                print(higiene)
                shortLoad()
                continuarConsulta = input("1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n")
                if continuarConsulta == "1":
                    load()
                elif continuarConsulta == "2":
                    shortLoad()
                    break
                elif continuarConsulta == "3":
                    exit()
                else:
                    print("Este comando é inválido. Retornando para Menu Principal.")
                    load()
                    continue
            else:
                print(f'{nomeUser}, essa categoria não existe. Tente novamente')
                continue

    # Configurando o Cadastro
    elif escolhaMenu == "2":
        while True:
            cadastrarProduto = input(f'{nomeUser}, gostaria de Cadastrar qual tipo de Produto?\n1- Alimentos\n2- Produtos de Limpeza\n3- Produtos de Higiene\n')
            if cadastrarProduto == "1":
                nomeProduto = input("Digite o nome do produto: ").upper()
                if nomeProduto in alimentos:
                    load()
                    print("Produto já cadastrado. Tente novamente.")
                    load()
                    continue


                elif nomeProduto not in alimentos:
                    print("Cadastrando o produto...")
                    alimentos.append(nomeProduto)
                    load()
                    print("Produto cadastrado com sucesso!")
                    shortLoad()
                    print("Atualizando lista...")
                    load()
                    break

            elif cadastrarProduto == "2":
                nomeProduto = input("Digite o nome do produto: ").upper()
                if nomeProduto in produtosDeLimpeza:
                    load()
                    print("Produto já cadastrado. Tente novamente.")
                    load()
                    continue


                elif nomeProduto not in produtosDeLimpeza:
                    print("Cadastrando o produto...")
                    produtosDeLimpeza.append(nomeProduto)
                    load()
                    print("Produto cadastrado com sucesso!")
                    shortLoad()
                    print("Atualizando lista...")
                    load()
                    break

            elif cadastrarProduto == "3":
                nomeProduto = input("Digite o nome do produto: ").upper()

                if nomeProduto in higiene:
                    load()
                    print("Produto já cadastrado. Tente novamente.")
                    load()
                    continue


                elif nomeProduto not in higiene:
                    print("Cadastrando o produto...")
                    higiene.append(nomeProduto)
                    load()
                    print("Produto cadastrado com sucesso!")
                    shortLoad()
                    print("Atualizando lista...")
                    load()
                    break

            else:
                print(f'{nomeUser}, essa categoria não existe. Tente novamente')
                shortLoad()
                continue

    #Consultando Deposito
    elif escolhaMenu == "3":
        print("Carregando deposito...")
        load()
        print(f'Deposito de alimentos: {alimentos}')
        shortLoad()
        print(f'Deposito de Produtos de Limpeza: {produtosDeLimpeza}')
        shortLoad()
        print(f'Deposito de Produtos de Higiene: {higiene}')
        shortLoad()

        escolhaDeposito = input ("1- Fechar Programa\n2- Voltar para o Menu\n")
        if escolhaDeposito == "1":
            exit()
        elif escolhaDeposito == "2":
            shortLoad()
            continue

    #Excluindo Produto
    elif escolhaMenu == "4":
        while True:
            opcaoExclusao = input("O que você deseja excluir?\n1- Alimentos\n2- Produtos de Limpeza\n3- Produtos de Higiene\n4- Voltar ao menu\n")
            if opcaoExclusao == "1":
                print(alimentos)
                produtoExclusao = input("O que deseja excluir?\n").upper()
                if produtoExclusao in alimentos:
                    print("Exluido produto...")
                    alimentos.remove(produtoExclusao)
                    load()
                    print("Atualizando lista...")
                    shortLoad()
                    print(alimentos)
                    print ("Produto excluido!")
                    shortLoad()
                    confirmarMenu = input("Deseja continuar excluindo?\n1- Sim\n2- Não\n")
                    if confirmarMenu == "1":
                        continue
                    elif confirmarMenu == "2":
                        print("Retornando ao Menu Principal...")
                        shortLoad()
                        break
                elif produtoExclusao not in alimentos:
                    print("Produto não existente.\nVoltando ao menu Exclusão")
                    shortLoad()
                    continue

            if opcaoExclusao == "2":
                print(produtosDeLimpeza)
                produtoExclusao = input("O que deseja excluir?\n").upper()
                if produtoExclusao in produtosDeLimpeza:
                    print("Exluido produto...")
                    produtosDeLimpeza.remove(produtoExclusao)
                    load()
                    print("Atualizando lista...")
                    shortLoad()
                    print(produtosDeLimpeza)
                    print ("Produto excluido!")
                    shortLoad()
                    confirmarMenu = input("Deseja continuar excluindo?\n1- Sim\n2- Não\n")
                    if confirmarMenu == "1":
                        continue
                    elif confirmarMenu == "2":
                        print("Retornando ao Menu Principal...")
                        shortLoad()
                        break
                elif produtoExclusao not in produtosDeLimpeza:
                    print("Produto não existente.\nVoltando ao menu Exclusão")
                    shortLoad()
                    continue

            if opcaoExclusao == "3":
                print(higiene)
                produtoExclusao = input("O que deseja excluir?\n").upper()
                if produtoExclusao in higiene:
                    print("Exluido produto...")
                    higiene.remove(produtoExclusao)
                    load()
                    print("Atualizando lista...")
                    shortLoad()
                    print(higiene)
                    print ("Produto excluido!")
                    shortLoad()
                    confirmarMenu = input("Deseja continuar excluindo?\n1- Sim\n2- Não\n")
                    if confirmarMenu == "1":
                        continue
                    elif confirmarMenu == "2":
                        print("Retornando ao Menu Principal...")
                        shortLoad()
                        break
                elif produtoExclusao not in higiene:
                    print("Produto não existente.\nVoltando ao menu Exclusão")
                    shortLoad()
                    continue




    else:
        print(f'{nomeUser}, essa escolha não existe. Tente Novamente.')
        shortLoad()
        continue
