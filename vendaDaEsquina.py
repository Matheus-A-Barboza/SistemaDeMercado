from time import sleep

# Funcoes
def load():
    sleep(5)


# Listas
alimentos = ["ARROZ", "FEIJAO", "MACARRAO", "CARNE"]
produtosDeLimpeza = ["AGUA SANITARIA", "DESINFETANTE", "DETERGENTE"]
higiene = ["PAPEL HIGIENICO", "ESCOVA DE DENTES", "SABONETE EM BARRA"]

# Codigo

nomeUser = input("Olá, Usuário. Qual seu nome?\n")

while True:
    escolhaMenu = input(
        f'Olá, {nomeUser}. O que você gostaria de fazer?\n1- Consultar Produtos\n2- Cadastrar Produtos\n3- Ver Deposito')

    # Configurando a Consulta
    if escolhaMenu == "1":
        while True:
            escolhaConsulta = input(
                f'{nomeUser}, o que gostaria de Consultar?\n1- Alimentos\n2- Produtos de Limpeza\n3- Produtos de Higiene\n')
            if escolhaConsulta == "1":
                load()
                print(alimentos)
                continuarConsulta = input("1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n")
                if continuarConsulta == "1":
                    load()
                elif continuarConsulta == "2":
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
                continuarConsulta = input("1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n")
                if continuarConsulta == "1":
                    load()
                elif continuarConsulta == "2":
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
                continuarConsulta = input("1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n")
                if continuarConsulta == "1":
                    load()
                elif continuarConsulta == "2":
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
                    load()
                    print("Produto cadastrado com sucesso!")
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
                    load()
                    print("Produto cadastrado com sucesso!")
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
                    load()
                    print("Produto cadastrado com sucesso!")
                    load()
                    break

            else:
                print(f'{nomeUser}, essa categoria não existe. Tente novamente')
                continue

    elif escolhaMenu == "3":
        input()
        print(alimentos)


    else:
        print(f'{nomeUser}, essa escolha não existe. Tente Novamente.')
        continue
