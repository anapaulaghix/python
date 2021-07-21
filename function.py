# definição
from random import random


def joga_moeda():
    if random() > 0.5:
        return 'cara'
    return 'coroa'


def diz_oi():
    print('olá mundo!')
    print('você é especial!')
    return 'Oi!'


def quadrado_7():
    # print(7 * 7)  # refatorar
    return 7 * 7


# parametro
def quadrado(numero):
    return numero * 2


def parabens(aniversariante):
    print(f"Parabéns {aniversariante}")


def maior(* num):  # args
    cont = big = 0
    for valor in num:
        print(f" {valor}")
        if cont == 0:
            big = valor
        else:
            if valor > big:
                big = valor
        cont = cont + 1
    print(f"Foram lidos {cont} valores")
    print(f"O maior valor foi {big}")


def sub(a, b):
    return a - b


def nome(name, sobrenome):   # keyword
    return f"Seu nome completo é {name} {sobrenome}"


# chamada de execução
diz_oi()
for n in range(1):
    diz_oi()
alguem = input("Qual seu nome? ")
print(diz_oi() + alguem)

print(quadrado(7))
print(quadrado(15))
print(joga_moeda())
parabens("Pedro")
maior(1, 2, 4, 5)
print(sub(38, 16))
print(nome(sobrenome="Ghiraldelli", name="Ana Paula"))

# variavel
ret = quadrado_7()
print(f'return: {ret}')

print(f'return: {quadrado_7() + 1}')