lista1 = [1, 22, 44, 78, 88, 0, 1, 0, 1]
lista2 = ['a', 'n', 'a', ' ', 'p', 'a', 'u', 'l', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('ana paula')

# verificar determinado valor nas listas
num = 10
if num in lista4:
    print(f"i find number {num}")
else:
    print(f"i dont find number {num}")

# iterar sobre listas
soma = 0
for element in lista1:
    soma = soma + element
print(soma)

soma = ''
for element in lista2:
    soma = soma + element
print(soma)

shopping = []
product = ''
while product != 'exit':
    print("Add a product on list or type 'exit': ")
    product = input()
    if product != "exit":
        shopping.append(product)
for product in shopping:
    print(shopping)

colors = ["purple", "black", "white", "red"]
for cor in colors:
    print(cor)

index = 0
while index < len(colors):
    print(colors[index])
    index = index + 1

# gerar indice em for
for index, cor in enumerate(colors):
    print(index, cor)

# ordenar valores
print(sum(lista1))
print(max(lista1))
print(min(lista1))
print(len(lista1))

lista1.sort()
print(lista1)

lista1.reverse()
print(lista1)

print(lista1.count(1))
print(lista5.count('a'))

print(lista1[::-1])

lista6 = lista2.copy()
print(lista6)

lista5.pop()
lista5.pop(2)
print(lista5)

# não substitui o valor inicial
lista1.insert(2, 'novo valor')
print(lista1)

# juntar duas listas
lista7 = lista1 + lista2
print(lista7)

# shallow copy, deep copy
new = lista1
new.append(4)
new = lista1.copy()
new.append(4)

# adicionar elementos
lista1.extend([123, 2, 3])
print(lista1)

print(lista1)
lista1.append(34)  # elemento unico
print(lista1)

lista1.append([1, 2, 3])
print(lista1)

if [1, 2, 3] in lista1:
    print("found the list")
else:
    print("didn't find the list")
