from time import sleep


def load() -> None:
    sleep(3)


def shortLoad() -> None:
    sleep(1.5)


# Início do programa
if __name__ == '__main__':
    # Produtos
    alimentos: list[str] = ['ARROZ', 'FEIJAO', 'MACARRAO', 'CARNE']
    produtos_de_limpeza: list[str] = [
        'AGUA SANITARIA',
        'DESINFETANTE',
        'DETERGENTE',
    ]
    higiene: list[str] = [
        'PAPEL HIGIENICO',
        'ESCOVA DE DENTES',
        'SABONETE EM BARRA',
    ]

    nome_user: str = input('Olá, Usuário. Qual seu nome?\n')
    shortLoad()

    while True:
        escolha_menu: str = input(
            f'Olá, {nome_user}. O que você gostaria de fazer?\n'
            '1 - Consultar Produtos\n'
            '2 - Cadastrar Produtos\n'
            '3 - Ver Deposito\n'
            '4 - Excluir Produto\n'
        )
        shortLoad()

        # Configurando a Consulta
        match escolha_menu:
            case '1':
                while True:
                    escolha_consulta: str = input(
                        f'{nome_user}, o que gostaria de Consultar?\n'
                        '1- Alimentos\n'
                        '2- Produtos de Limpeza\n'
                        '3- Produtos de Higiene\n'
                    )
                    match escolha_consulta:
                        case '1':
                            load()
                            print(alimentos)
                            shortLoad()

                            continuar_consulta = input(
                                '1- Continuar Consultando\n2- Voltar ao Menu\n3- Encerrar Programa\n'
                            )

                            match continuar_consulta:
                                case '1':
                                    load()
                                case '2':
                                    shortLoad()
                                    break
                                case '3':
                                    exit()
                                case _:
                                    print(
                                        'Este comando é inválido. Retornando para Menu Principal.'
                                    )
                                    load()
                                    continue

                        case '2':
                            load()
                            print(produtos_de_limpeza)
                            shortLoad()

                            continuar_consulta = input(
                                '1- Continuar Consultando\n'
                                '2- Voltar ao Menu\n'
                                '3- Encerrar Programa\n'
                            )

                            match continuar_consulta:
                                case '1':
                                    load()
                                case '2':
                                    shortLoad()
                                    break
                                case '3':
                                    exit()
                                case _:
                                    print(
                                        'Este comando é inválido. Retornando para Menu Principal.'
                                    )
                                    load()
                                    continue

                        case '3':
                            load()
                            print(higiene)
                            shortLoad()

                            continuar_consulta = input(
                                '1- Continuar Consultando\n'
                                '2- Voltar ao Menu\n'
                                '3- Encerrar Programa\n'
                            )

                            match continuar_consulta:
                                case '1':
                                    load()
                                case '2':
                                    shortLoad()
                                    break
                                case '3':
                                    exit()
                                case _:
                                    print(
                                        'Este comando é inválido. Retornando para Menu Principal.'
                                    )
                                    load()
                                    continue
                        case _:
                            print(
                                f'{nome_user}, essa categoria não existe. Tente novamente'
                            )
                            continue

            # Configurando o Cadastro
            case '2':
                while True:
                    cadastrar_produto: str = input(
                        f'{nome_user}, gostaria de Cadastrar qual tipo de Produto?\n'
                        '1- Alimentos\n'
                        '2- Produtos de Limpeza\n'
                        '3- Produtos de Higiene\n'
                    )

                    match cadastrar_produto:
                        case '1':
                            nome_produto: str = input(
                                'Digite o nome do produto: '
                            ).upper()

                            if nome_produto in alimentos:
                                load()
                                print(
                                    'Produto já cadastrado. Tente novamente.'
                                )
                                load()
                                continue

                            else:
                                print('Cadastrando o produto...')
                                alimentos.append(nome_produto)
                                load()
                                print('Produto cadastrado com sucesso!')
                                shortLoad()
                                print('Atualizando lista...')
                                load()
                                break

                        case '2':
                            nome_produto = input(
                                'Digite o nome do produto: '
                            ).upper()

                            if nome_produto in produtos_de_limpeza:
                                load()
                                print(
                                    'Produto já cadastrado. Tente novamente.'
                                )
                                load()
                                continue

                            else:
                                print('Cadastrando o produto...')
                                produtos_de_limpeza.append(nome_produto)
                                load()
                                print('Produto cadastrado com sucesso!')
                                shortLoad()
                                print('Atualizando lista...')
                                load()
                                break

                        case '3':
                            nome_produto = input(
                                'Digite o nome do produto: '
                            ).upper()

                            if nome_produto in higiene:
                                load()
                                print(
                                    'Produto já cadastrado. Tente novamente.'
                                )
                                load()
                                continue

                            else:
                                print('Cadastrando o produto...')
                                higiene.append(nome_produto)
                                load()
                                print('Produto cadastrado com sucesso!')
                                shortLoad()
                                print('Atualizando lista...')
                                load()
                                break

                        case _:
                            print(
                                f'{nome_user}, essa categoria não existe. Tente novamente'
                            )
                            shortLoad()
                            continue

            # Consultando Deposito
            case '3':
                print('Carregando deposito...')
                load()
                print(f'Deposito de alimentos: {alimentos}')
                shortLoad()
                print(
                    f'Deposito de Produtos de Limpeza: {produtos_de_limpeza}'
                )
                shortLoad()
                print(f'Deposito de Produtos de Higiene: {higiene}')
                shortLoad()

                escolha_deposito = input(
                    '1- Fechar Programa\n2- Voltar para o Menu\n'
                )

                match escolha_deposito:
                    case '1':
                        exit()
                    case '2' | _:
                        shortLoad()
                        continue

            # Excluindo Produto
            case '4':
                while True:
                    opcao_exclusao: str = input(
                        'O que você deseja excluir?\n'
                        '1- Alimentos\n'
                        '2- Produtos de Limpeza\n'
                        '3- Produtos de Higiene\n'
                        '4- Voltar ao menu\n'
                    )

                    match opcao_exclusao:
                        case '1':
                            print(alimentos)

                            produto_exclusao: str = input(
                                'O que deseja excluir?\n'
                            ).upper()

                            if produto_exclusao in alimentos:
                                print('Exluido produto...')
                                alimentos.remove(produto_exclusao)
                                load()
                                print('Atualizando lista...')
                                shortLoad()
                                print(alimentos)
                                print('Produto excluido!')
                                shortLoad()

                                confirmar_menu: str = input(
                                    'Deseja continuar excluindo?\n1- Sim\n2- Não\n'
                                )

                                if confirmar_menu == '1':
                                    continue
                                else:
                                    print('Retornando ao Menu Principal...')
                                    shortLoad()
                                    break
                            else:
                                print(
                                    'Produto não existente.\nVoltando ao menu Exclusão'
                                )
                                shortLoad()
                                continue

                        case '2':
                            print(produtos_de_limpeza)

                            produto_exclusao = input(
                                'O que deseja excluir?\n'
                            ).upper()

                            if produto_exclusao in produtos_de_limpeza:
                                print('Exluido produto...')
                                produtos_de_limpeza.remove(produto_exclusao)
                                load()
                                print('Atualizando lista...')
                                shortLoad()
                                print(produtos_de_limpeza)
                                print('Produto excluido!')
                                shortLoad()

                                confirmar_menu = input(
                                    'Deseja continuar excluindo?\n1- Sim\n2- Não\n'
                                )

                                if confirmar_menu == '1':
                                    continue
                                else:
                                    print('Retornando ao Menu Principal...')
                                    shortLoad()
                                    break
                            else:
                                print(
                                    'Produto não existente.\nVoltando ao menu Exclusão'
                                )
                                shortLoad()
                                continue

                        case '3':
                            print(higiene)

                            produto_exclusao = input(
                                'O que deseja excluir?\n'
                            ).upper()

                            if produto_exclusao in higiene:
                                print('Exluido produto...')
                                higiene.remove(produto_exclusao)
                                load()
                                print('Atualizando lista...')
                                shortLoad()
                                print(higiene)
                                print('Produto excluido!')
                                shortLoad()

                                confirmar_menu = input(
                                    'Deseja continuar excluindo?\n1- Sim\n2- Não\n'
                                )

                                if confirmar_menu == '1':
                                    continue
                                else:
                                    print('Retornando ao Menu Principal...')
                                    shortLoad()
                                    break
                            elif produto_exclusao not in higiene:
                                print(
                                    'Produto não existente.\nVoltando ao menu Exclusão'
                                )
                                shortLoad()
                                continue
            case _:
                print(
                    f'{nome_user}, essa escolha não existe. Tente Novamente.'
                )
                shortLoad()
                continue
