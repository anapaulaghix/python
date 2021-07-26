# list comprehension
numbers = [1, 2, 3, 4, 5, 6]
res = [number * 10 for number in numbers]
print(res)


def funcao(valor):
    return valor * valor


res1 = [funcao(number) for number in numbers]
print(res)

# em loop
numeros_dobrados = []
for number in numbers:
    numeros_dobrados.append(number * 2)
print(numeros_dobrados)

# em list comprehension
print([number * 2 for number in numbers])

pares = [number for number in numbers if number % 2 == 0]
impares = [number for number in numbers if number % 2 != 0]
print(pares)
print(impares)

# dictonary comprehension
quadrados = {valor: valor ** 2 for valor in numbers}
print(quadrados)

valores = [1, 2, 3, 4, 5]

chaves = "abcde"
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

res2 = {num: ('par' if num % 2 == 0 else 'impar') for num in valores}
print(res)
