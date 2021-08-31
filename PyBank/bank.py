from typing import List
from time import sleep
from models.client import Cliente
from models.account import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print(
        '\n====================================='
        '\n=============== ATM ================='
        '\n============= Py Bank ==============='
        '\n====================================='
    )

    opcao: int = int(
        input(
            '\nSelecione uma opção no menu:'
            '\n1 - Criar Conta'
            '\n2 - Efetuar Saque'
            '\n3 - Efetuar Depósito'
            '\n4 - Efetuar Transferência'
            '\n5 - Listar Contas'
            '\n6 - Sair do Sistema\n> '
        ))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('\nMuito obrigado por usar o PyBank. Volte sempre! =)')
        sleep(3)
        exit(0)
    else:
        print(
            '\nLamento mas a opção selecionada é inválida. Por favor tente '
            'novamente.'
        )
        sleep(3)
        menu()


def criar_conta() -> None:
    print('\nInforme os dados do cliente:')

    nome: str = input('Nome do cliente:\n> ')
    email: str = input('E-mail do cliente:\n> ')
    cpf: str = input('CPF do cliente:\n> ')
    data_nascimento: str = input('Data de nascimento:\n> ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print(
        '\nConta criada com sucesso!\nDados da conta:\n-----------------------'
    )

    print(conta)

    sleep(3)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('\nInforme o número da sua conta:\n> '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('\nInforme o valor do saque:\n> '))
            conta.sacar(valor)

        else:
            print(
                f'\nA conta de número {numero} não foi encontrada. '
                f'Tente novamente.'
            )
            sleep(3)
            menu()

    else:
        print('\nAinda não existem contas cadastradas.')

    sleep(3)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('\nInforme o número da conta:\n> '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('\nInforme o valor do depósito:\n> '))
            conta.depositar(valor)

        else:
            print(
                f'\nA conta de número {numero} não foi encontrada. '
                f'Tente novamente.'
            )
            sleep(3)
            menu()

    else:
        print('\nAinda não existem contas cadastradas.')

    sleep(3)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(
            input('\nInforme o número da conta de origem:\n> ')
        )

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input(
                '\nInforme o número da conta de destino:\n> '
            ))

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input(
                    '\nInforme o valor a transferir:\n> '
                ))

                conta_origem.transferir(conta_destino, valor)

            else:
                print(
                    f'\nA conta de destino com número {numero_destino} '
                    f'não foi encontrada. Tente novamente.')

            sleep(3)
            menu()

        else:
            print(
                f'\nA conta de número {numero_origem} não foi encontrada. '
                f'Tente novamente.'
            )

        sleep(3)
        menu()

    else:
        print('\nAinda não existem contas cadastradas.')

    sleep(3)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('\nListagem de contas\n--------------------')

        for conta in contas:
            print(conta)
            print('------------------')
            sleep(1)
    else:
        print(
            '\nNão existem contas cadastradas'
        )

    sleep(3)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
