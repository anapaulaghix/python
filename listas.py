lista1 = [1, 22, 44, 78, 88, 0, 1, 0, 1]
lista2 = ['a', 'n', 'a', ' ', 'p', 'a', 'u', 'l', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('ana paula')

# verfiicar determinado valor nas listas
num = 10
if num in lista4:
    print(f"i find number {num}")
else:
    print(f"i dont find number {num}")

# ordenar valores
lista1.sort()
print(lista1)

print(lista1.count(1))
print(lista5.count('a'))

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

# não substitui o valor inicial
lista1.insert(2, 'novo valor')
print(lista1)


num = int(input("Enter a number: "))
n = 0
vet = []
vet2 = []
for i in range(1, num+1):
    if i % 2 == 1 or i == 2:
        vet.append(i)
for i in range(0, len(vet)):
    if vet[i] > 1:
        vet2.append(vet[i])
if vet == 1:
    print("invalid")
elif vet2[len(vet2)-1] == num:
    print("Prime number!")
else:
    print("it's not prime")
