nome = input("Qual seu nome? ")
print(f"Seja Bem Vindo(a) {nome}")

idade = int(input("Qual sua idade? "))
print(f"Você tem {idade} anos")

print(f"{nome} nasceu em {2021 - idade}")

# input() -> Todo dado recebido via input é do tipo String

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (M) "))
imc = peso / (altura**2)
print("O imc é {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO do peso normal")
elif 18.5 <= imc < 25:
    print("Parabéns, você está na faixa de peso normal")
elif 25 <= imc < 30:
    print("Você está em sobrepeso")
elif 30 <= imc < 40:
    print("Você está em obesidade")
elif imc <= 40:
    print("Você está em obesidade mórbida, cuidado!")

print("Nota dos alunos")
nota1 = float(input("Primeira Nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1} e {nota2}, a média do aluno é {media}")
if 7 > media >= 5:
    print("O aluno está em recuperação")
elif media >= 7:
    print("O aluno está aprovado")
elif media < 5:
    print("O aluno está reprovado")
