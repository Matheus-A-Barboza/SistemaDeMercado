#Código desenvolvido por: @programmerantunes
#LinkedIn: www.linkedin.com/Matheus-A-Barboza
#GitHub: www.github.com/Matheus-A-Barboza
#Feedback's através das redes sociais

from time import sleep
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='sistemavendas',
)

cursor = conexao.cursor()


def shortLoad():
    sleep(2)


print('------------------------------------------------')
print('-------------Bem-Vindo(a) ao Sistema------------')
print('------------------------------------------------')
shortLoad()

nome_user = input("Olá, Usuário. Qual seu nome?\n")
shortLoad()

while True:

    escolha_menu = input(
        f'Olá, {nome_user}. O que você gostaria de fazer?\n'
        '1 - Consultar Produtos\n'
        '2 - Cadastrar Produtos\n'
        '3 - Atualizar Produtos\n'
        '4 - Ver Deposito\n'
        '5 - Excluir Produto\n'
        '6 - Sair do Programa\n')
    shortLoad()

    # Configurando a Consulta
    if escolha_menu == '1':
        while True:
            continuar_consulta = input(
                f'{nome_user}, o que gostaria de Consultar?\n'
                '1 - Alimentos\n'
                '2 - Produtos de Limpeza\n'
                '3 - Produtos de Higiene\n')

            if continuar_consulta == '1':
                print('Buscando Alimentos no Deposito...')
                shortLoad()

                deposito_alimentos = f'SELECT * FROM alimentos'
                cursor.execute(deposito_alimentos)
                resultado = cursor.fetchall()
                print(resultado)
                shortLoad()

                continuar_consulta = input('1 - Continuar Consultando\n'
                                           '2 - Voltar ao Menu\n'
                                           '3 - Encerrar Programa\n')

                if continuar_consulta == '1':
                    shortLoad()
                elif continuar_consulta == '2':
                    shortLoad()
                    break
                elif continuar_consulta == '3':
                    print('Fechando Programa...')
                    shortLoad()
                    exit()
                else:
                    print('Este comando é inválido.\n'
                          'Retornando para Menu Principal.')
                    shortLoad()
                    continue

            elif continuar_consulta == '2':
                shortLoad()

                print('Buscando Produtos de Limpeza no Deposito...')
                deposito_limpeza = f'SELECT * FROM limpeza'
                cursor.execute(deposito_limpeza)
                resultado = cursor.fetchall()
                print(resultado)
                shortLoad()

                continuar_consulta = input('1 - Continuar Consultando\n'
                                           '2 - Voltar ao Menu\n'
                                           '3 - Encerrar Programa\n')
                if continuar_consulta == '1':
                    shortLoad()
                elif continuar_consulta == '2':
                    shortLoad()
                    break
                elif continuar_consulta == '3':
                    print('Fechando Programa...')
                    shortLoad()
                    exit()
                else:
                    print('Este comando é inválido.\n'
                          'Retornando para Menu Principal.')
                    shortLoad()
                    continue

            elif continuar_consulta == '3':
                shortLoad()

                print('Buscando Produtos de Higiene no Deposito...')
                deposito_higiene = f'SELECT * FROM higiene'
                cursor.execute(deposito_higiene)
                resultado = cursor.fetchall()
                print(resultado)
                shortLoad()

                continuar_consulta = input(
                    '1 - Continuar Consultando\n'
                    '2 - Voltar ao Menu\n'
                    '3 - Encerrar Programa\n'
                    )
                
                if continuar_consulta == "1":
                    shortLoad()
                elif continuar_consulta == "2":
                    shortLoad()
                    break
                elif continuar_consulta == "3":
                    print('Fechando Programa...')
                    shortLoad()
                    exit()
                else:
                    print("Este comando é inválido. Retornando para Menu Principal.")
                    shortLoad()
                    continue
            else:
                print(f'{nome_user}, essa categoria não existe. Tente novamente')
                continue

    # Configurando o Cadastro
    elif escolha_menu == "2":
        while True:
            cadastrar_produto = input(
                f'{nome_user}, gostaria de Cadastrar qual tipo de Produto?\n'
                '1 - Alimentos\n'
                '2 - Produtos de Limpeza\n'
                '3 - Produtos de Higiene\n'
                )
            
            if cadastrar_produto == "1":
                nome_produto = input("Digite o nome do produto: ").upper()
                qnt_produto = input("Qual a quantidade a ser adicionada? ")
                cadastrar = f"SELECT nome_produto FROM deposito WHERE nome_produto = '{nome_produto}'"

                print("Cadastrando o produto...")
                shortLoad()
                cadastro_produto = "INSERT INTO cadastrarprodutos (nome_produto, tipo_produto, qnt_produto) VALUES (%s,'ALIMENTOS',%s)"
                cadastro1 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_produto, cadastro1)

                cadastro_deposito = "INSERT INTO deposito (nome_produto, tipo_produto, qnt_produto) VALUES (%s,'ALIMENTOS', %s)"
                cadastro2 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_deposito, cadastro2)

                cadastro_alimento = "INSERT INTO alimentos (nome_alimento, qnt_alimento) VALUES (%s, %s)"
                cadastro3 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_alimento, cadastro3)

                conexao.commit()
                conexao.close()

                print("Produto cadastrado com sucesso!")
                shortLoad()
                print("Atualizando lista...")
                shortLoad()
                break

            elif cadastrar_produto == "2":
                nome_produto = input("Digite o nome do produto: ").upper()
                qntProduto = input("Qual a quantidade a ser adicionada? ")
                cadastrar = f"SELECT nome_produto FROM deposito WHERE nome_produto = '{nome_produto}'"

                print("Cadastrando o produto...")
                shortLoad()
                cadastro_produto = "INSERT INTO cadastrarprodutos (nome_produto, tipo_produto, qnt_produto) VALUES (%s,'LIMPEZA',%s)"
                cadastro1 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_produto, cadastro1)

                cadastro_deposito = "INSERT INTO deposito (nome_produto, tipo_produto, qnt_produto) VALUES (%s,'LIMPEZA', %s)"
                cadastro2 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_deposito, cadastro2)

                cadastro_alimento = "INSERT INTO limpeza (nome_produto, qnt_produto) VALUES (%s, %s)"
                cadastro3 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_alimento, cadastro3)

                conexao.commit()
                conexao.close()

                print("Produto cadastrado com sucesso!")
                shortLoad()
                print("Atualizando lista...")
                shortLoad()
                break

            elif cadastrar_produto == "3":
                nome_produto = input("Digite o nome do produto: ").upper()
                qnt_produto = input("Qual a quantidade a ser adicionada? ")
                cadastrar = f"SELECT nome_produto FROM deposito WHERE nome_produto = '{nome_produto}'"

                print("Cadastrando o produto...")
                shortLoad()
                cadastro_produto = "INSERT INTO cadastrarprodutos (nome_produto, tipo_produto, qnt_produto) VALUES (%s,'HIGIENE',%s)"
                cadastro1 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_produto, cadastro1)

                cadastro_deposito = "INSERT INTO deposito (nome_produto, tipo_produto, qnt_produto) VALUES (%s,'HIGIENE', %s)"
                cadastro2 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_deposito, cadastro2)

                cadastro_alimento = "INSERT INTO higiene (nome_produto, qnt_produto) VALUES (%s, %s)"
                cadastro3 = (nome_produto, qnt_produto)
                cursor.execute(cadastro_alimento, cadastro3)

                conexao.commit()
                conexao.close()

                print("Produto cadastrado com sucesso!")
                shortLoad()
                print("Atualizando lista...")
                shortLoad()
                break

            else:
                print(f'{nome_user}, essa categoria não existe. Tente novamente')
                shortLoad()
                continue

    # UPDATE
    elif escolha_menu == "3":
        comando = 'SELECT * FROM deposito'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

        atualizar_produto = input(
            "Digite o nome do Produto para atualizar: ").upper()
        atualizar_qnt = input("Digite a nova quantidade: ")
        atualizar_db = (
            f"UPDATE deposito SET qnt_produto = '{atualizar_qnt}' WHERE nome_produto = '{atualizar_produto}'")
        cursor.execute(atualizar_db)
        conexao.commit()
        shortLoad()
        print("Atualizando Deposito...")
        shortLoad()
        print("Deposito Atualizado!")

    # Consultando Deposito
    elif escolha_menu == "4":
        print("Carregando deposito...")
        shortLoad()
        
        print("Deposito de Alimentos:")
        abrir_deposito = f"SELECT * FROM alimentos"
        shortLoad()
        cursor.execute(abrir_deposito)
        resultado = cursor.fetchall()
        print(resultado)
        shortLoad()
        print('\n')
        
        print("Deposito de Limpeza:")
        abrir_deposito = f"SELECT * FROM limpeza"
        shortLoad()
        cursor.execute(abrir_deposito)
        resultado = cursor.fetchall()
        print(resultado)
        shortLoad()
        print('\n')
        
        print("Deposito de Higiene:")
        abrir_deposito = f"SELECT * FROM higiene"
        shortLoad()
        cursor.execute(abrir_deposito)
        resultado = cursor.fetchall()
        print(resultado)
        shortLoad()

        escolhaDeposito = input('1 - Fechar Programa\n'
                                '2 - Voltar para o Menu\n'
                                )
        
        if escolhaDeposito == "1":
            print('Fechando Programa...')
            shortLoad()
            exit()
        elif escolhaDeposito == "2":
            shortLoad()
            continue

    # DELETE
    elif escolha_menu == "5":
        while True:
            opcao_exclusao = input(
                'O que você deseja excluir?\n'
                '1 - Alimentos\n'
                '2 - Produtos de Limpeza\n'
                '3 - Produtos de Higiene\n'
                '4 - Voltar ao menu\n'
                )
            
            if opcao_exclusao == "1":
                produto_deposito = "SELECT * FROM deposito WHERE tipo_produto = 'ALIMENTOS'"
                cursor.execute(produto_deposito)
                result = cursor.fetchall()
                print(result)

                produto_exclusao = input("O que deseja excluir?\n").upper()
                cursor.execute(
                    f"DELETE FROM deposito WHERE nome_produto = '{produto_exclusao}'")
                conexao.commit()

                print("Exluindo produto...")
                shortLoad()
                print("Atualizando lista...")
                shortLoad()

                produto_deposito = "SELECT * FROM deposito WHERE tipo_produto = 'ALIMENTOS'"
                cursor.execute(produto_deposito)
                result = cursor.fetchall()
                print(result)
                print("Produto excluido!")
                shortLoad()

                confirmar_menu = input(
                    'Deseja continuar excluindo?\n'
                    '1 - Sim\n'
                    '2 - Não\n'
                    )
                
                if confirmar_menu == "1":
                    continue
                elif confirmar_menu == "2":
                    print("Retornando ao Menu Principal...")
                    shortLoad()
                    break

            elif opcao_exclusao == "2":
                produto_deposito = "SELECT * FROM deposito WHERE tipo_produto = 'LIMPEZA'"
                cursor.execute(produto_deposito)
                result = cursor.fetchall()
                print(result)
                produto_exclusao = input("O que deseja excluir?\n").upper()
                cursor.execute(
                    f"DELETE FROM deposito WHERE nome_produto = '{produto_exclusao}'")
                conexao.commit()

                print("Excluindo produto...")
                shortLoad()
                print("Atualizando lista...")
                shortLoad()

                produto_deposito = "SELECT * FROM deposito WHERE tipo_produto = 'LIMPEZA'"
                cursor.execute(produto_deposito)
                result = cursor.fetchall()
                print(result)
                print("Produto excluido!")
                shortLoad()

                confirmar_menu = input(
                    'Deseja continuar excluindo?\n'
                    '1 - Sim\n'
                    '2 - Não\n'
                    )
                
                if confirmar_menu == "1":
                    continue
                elif confirmar_menu == "2":
                    print("Retornando ao Menu Principal...")
                    shortLoad()
                    break

            elif opcao_exclusao == "3":
                produto_deposito = "SELECT * FROM deposito WHERE tipo_produto = 'HIGIENE'"
                cursor.execute(produto_deposito)
                result = cursor.fetchall()
                print(result)
                produto_exclusao = input("O que deseja excluir?\n").upper()
                cursor.execute(
                    f"DELETE FROM deposito WHERE nome_produto = '{produto_exclusao}'")
                conexao.commit()

                print("Excluindo produto...")
                shortLoad()
                print("Atualizando lista...")
                shortLoad()

                produto_deposito = "SELECT * FROM deposito WHERE tipo_produto = 'HIGIENE'"
                cursor.execute(produto_deposito)
                result = cursor.fetchall()
                print(result)

                print("Produto excluído!")
                shortLoad()

                confirmar_menu = input(
                    'Deseja continuar excluindo?\n'
                    '1 - Sim\n'
                    '2 - Não\n'
                    )
                
                if confirmar_menu == "1":
                    continue

                elif confirmar_menu == "2":
                    print("Retornando ao Menu Principal...")
                    shortLoad()
                    break
            elif opcao_exclusao == '4':
                print('Retornando ao Menu Principal...')
                break
    elif escolha_menu == '6':
        print('Fechando Programa...')
        shortLoad()
        exit()

    else:
        print(f'{nome_user}, essa escolha não existe. Tente Novamente.')
        shortLoad()
        continue
