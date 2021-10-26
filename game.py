from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nivel de dificuldade desejado [1, 2, 3 ou 4]'))

    calc: Calcular = Calcular(dificuldade)

    print('informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int(input())
    if calc.chechar_resultado(resultado):
        pontos += 1
        print(f"você tem {pontos} ponto(s).")

    continuar: int = int(input("você deseja continuar jogando? [1 - sim / 0 - não]"))

    if continuar:
        jogar(pontos)
    else:
        print(f"você finalizou o jogo com {pontos} ponto(s).")
