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


# parametro obrigatório
def quadrado(numero):
    return numero * 2


# parametro padrão
def exponent(exponente, potencia=2):
    return exponente * potencia


def parabens(aniversariante):
    print(f"Parabéns {aniversariante}")


"""
*args coloca valores extras em uma tupla
**kwargs exige parametros nomeados e transforma valores extras em um dicionário
não são parametros obrigatórios
"""


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


def adder(*args):
    sum = 0

    for n in args:
        sum = sum + n

    print("Sum:", sum)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)


def coresfav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


def nome(name, sobrenome):   # keyword
    return f"Seu nome completo é {name} {sobrenome}"


total = 0


def incrementa():
    global total  # chamando a variável global
    total = total + 1
    return total


# chamada de execução
diz_oi()
for n in range(1):
    diz_oi()
alguem = input("Qual seu nome? ")
print(diz_oi() + alguem)

print(joga_moeda())
print(quadrado(7))
print(quadrado(15))
print(exponent(3))
print(exponent(2, 3))
parabens("Pedro")
maior(1, 2, 4, 5)
coresfav(ana='roxo', pedro='amarelo', julia='azul', vitor='verde')
print(nome(sobrenome="Ghiraldelli", name="Ana Paula"))
print(incrementa())

# variavel
ret = quadrado_7()
print(f'return: {ret}')

print(f'return: {quadrado_7() + 1}')

# tempo minimo em minutos para entrarem um um show
pessoas = int(input("Quantas pessoas? "))
segundos = float(input("Quantos segundos? "))
portoes = int(input("Quantos portoes? "))

def tempo_minimo_minutos(pessoas, segundos, portoes):
     tempo_total = pessoas * segundos
     tempo_minimo_segundos = tempo_total / portoes
     tempo_minimo_minutos = tempo_minimo_segundos / 60
     return tempo_minimo_minutos

print(f"Tempo minimo em minutos: {tempo_minimo_minutos(pessoas, segundos, portoes):.2f}")

# calcular distancia de som em milisegundos ate a ultima pessoa de um show
distancia_km = float(input("Qual a distancia em km? "))

def tempo_total_milisegundos(distancia_km):
    velocidade_som_ms = 340
    velocidade_som_kms = velocidade_som_ms / 1000
    tempo_total_segundos = distancia_km / velocidade_som_kms
    tempo_total_milisegundos = tempo_total_segundos * 1000
    return tempo_total_milisegundos

print(f"Tempo em milisegundos ouvidos pela ultima pessoa: {tempo_total_milisegundos(distancia_km):.2f}")
