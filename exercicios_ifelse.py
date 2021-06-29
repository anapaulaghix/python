print("Programa para eibir o maior número")
valorA = int(input("Digite um número: "))
valorB = int(input("Digite o segundo número: "))

if valorA > valorB:
    print(valorA)
else:
    print(valorB)

print("Programa para exibir o número par")
numero = int(input("Digite um número: "))

if (numero % 2) == 0:
    print("é um numero par")
else:
    print("é um numero ímpar")

print("Programa para exibir sua maioridade")
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("maior de idade")

print("Programa para exibir dobro triplo e raiz de um número")
n = int(input("Digite um número: "))
print(f"Dobro: {n*2}")
print(f"Triplo: {n*3}")
print(f"Raiz quadrada: {n**(1/2)}")
