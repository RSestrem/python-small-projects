from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input(
        'Informe o nível de dificuldade desejado [1, 2, 3 ou 4]:\n> '
    ))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()  # no terminal teremos por exemplo: 5 + 4 = ?

    resultado: int = int(input('> '))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).\n')

    continuar: int = int(input(
        'Deseja continuar no jogo? [1 - sim; 0 - não]\n> '
    ))

    while continuar not in (0, 1):
        continuar: int = int(input(
            '\nEssa não é uma opção válida.\n'
            'Por favor selecione 1 para continuar'
            ' ou 0 para parar de jogar:\n> '
        ))

    if continuar:
        jogar(pontos)
    else:
        print(
            f'Você finalizou com {pontos} ponto(s).\n'
            f'Muito obrigado e até a próxima! =)'
        )


if __name__ == '__main__':
    main()
