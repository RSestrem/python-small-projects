from typing import List, Dict
from time import sleep

from models.product import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []
""" caso o usuário adicione mais de uma unidade de um mesmo produto, o
dicionário manterá a mesma chave Produto e incrementará o valor de int"""


def main() -> None:
    menu()


def menu() -> None:
    print(
        '\n====================================\n'
        '========== Bem-vindo(a) ============\n'
        '========== Python Shop  ============\n'
        '====================================\n'
    )

    opcao: int = int(input(
        'Selecione uma das opções abaixo:\n\n'

        '1 - Cadastrar produto(s)\n'
        '2 - Listar produto(s)\n'
        '3 - Comprar produto(s)\n'
        '4 - Visualizar carrinho\n'
        '5 - Fechar pedido\n'
        '6 - Sair do sistema\n> '
    ))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print(
            '\nMuito obrigado(a) por comprar no Python Shop. Volte sempre! =)'
        )
        sleep(3)  # vai parar a aplicação por 2 segundos e sair do sistema
        exit(0)
    else:
        print('Opção inválida. Por favor tente novamente.')
        sleep(3)  # vai parar a aplicação por 3 segundos e reiniciar o menu
        menu()


def cadastrar_produto() -> None:
    print('\nCadastro de Produto\n===================')

    nome: str = input('Informe o nome do produto:\n> ')
    preco: float = float(input('Informe o preço do produto:\n> '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'\nO produto {produto.nome} foi cadastrado com sucesso!')
    sleep(3)  # para a aplicação por 3 segundos antes de reiniciar o menu
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos\n--------------------')

        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)

    else:
        print('\nAinda não existem produtos cadastrados')
    sleep(3)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print(
            '\nInforme o código do produto que deseja adicionar ao carrinho:\n'
            '-------------------------------------------------------------\n'
            '=================== Produtos Disponíveis ====================\n'
        )

        for produto in produtos:
            print(produto)
            print('------------------------------------------------------')
            sleep(1)

        codigo: int = int(input('\n> '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False

                for item in carrinho:
                    quant: int = item.get(produto)

                    if quant:
                        item[produto] = quant + 1
                        print(
                            f'O produto {produto.nome} agora possui '
                            f'{quant + 1} unidades no carrinho.'
                        )

                        tem_no_carrinho = True
                        sleep(3)
                        menu()

                if not tem_no_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)

                    print(
                        f'\nO produto {produto.nome} foi adicionado ao carrinho'
                    )

                    sleep(3)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)

                print(
                    f'\nO produto {produto.nome} foi adicionado ao carrinho.'
                )

                sleep(3)
                menu()

        else:
            print(
                f'\nO produto com o código informado '
                f'({codigo}) não foi encontrado.'
            )

            sleep(3)
            menu()

    else:
        print('\nNão existem produtos cadastrados no catálogo.')

    sleep(3)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('\nProdutos no carrinho:')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)

    else:
        print('\nAinda não existem produtos no carrinho')

    sleep(3)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0.0

        print('\nProdutos do carrinho')

        for item in carrinho:
            for data in item.items():
                print(data[0])  # retorna somente o nome do produto
                print(f'Quantidade: {data[1]}')
                valor_total += data[0].preco * data[1]
                print('-----------------------')
                sleep(1)

        print(
            f'\nO valor do seu pedido é: '
            f'{formata_float_str_moeda(valor_total)}'
        )

        print(
            '\nMuito obrigado(a) por comprar no Python Shop. Volte sempre! =)'
        )

        carrinho.clear()
        sleep(5)

    else:
        print('\nO carrinho está vazio.')
    sleep(3)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for element in produtos:
        if element.codigo == codigo:
            p = element

    return p


if __name__ == '__main__':
    main()
