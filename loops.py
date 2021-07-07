# for
name = "ana"
lista = [1, 3, 5, 7, 9]
numbers = range(1, 10)

for letter in name:
    print(letter)

for number in lista:
    print(number)

for number in range(1, 11):
    print(number)

for i in range(3, 16, 3):
    print(i)

for number in range(10, 0, -1):
    print(number)

for number in range(1, 11):
    if number == 6:
        break
    else:
        print(number)
print("Got out of loop!")

# ex 1
num = int(input("Enter a number: "))
cont = 0
for cont in range(1, num+1):
    if cont % 2 == 0:
        print(cont)

# ex 2
qtd = int(input("How many times will this loop run? "))
soma = 0
for i in range(1, qtd+1):
    numr = int(input(f"print the {i}/{qtd} value: "))
    soma = soma + numr
print(f"The sum is {soma}")

# ex 3
qntd = int(input("Enter a number: "))
raiz = 0
for i in range(1, qntd+1):
    raiz = raiz + qntd
print(f"square root: {raiz}")

# while
numero = 1
while numero < 11:
    print(numero)
    numero = numero + 1
print("The end!!!")

answer = " "
while answer != "yes":
    answer = input("This is the end? ")

while True:
    comand = input("Write 'Ana' to exit: ")
    if comand == "Ana":
        break

carrinho_compras = []
produto = ''
while produto != 'exit':
    print('add a product to the list or type "exit" to exit: ')
    produto = input()
    carrinho_compras.append(produto)
for produto in carrinho_compras:
    print(produto)
