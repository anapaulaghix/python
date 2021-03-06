from passlib.hash import pbkdf2_sha256 as cryp
"""
Orientaçào a objetos em python
- classes: um modelo que os objetos devem seguir
- métodos: comportaento do objeto (funcões, def)
- construtor: método especial utilizado para criar objetos
- atributos: características do objeto, ex: nome, cor, preço, etc.
- objetos: instância de uma classe específica.

4 pilares:
Abstração, Encapsulamento, Herança e Polimorfismo 
"""


class Lampada:    # objeto = lâmpada
    def __init__(self, voltagem, cor):   # método
        self.voltagem = voltagem   # atributos
        self.cor = cor
        self.ligada = False


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("saldo insuficiente")
        else:
            print('Valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor


class Produto:
    imposto = 1.05  # Atributos de classe/estáticos
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

    def desconto(self, porcentagem):
        """retorna o valor do produto com o desconto"""
        return (self.valor * (100 - porcentagem)) / 100


p1 = Produto('Playstation', 'Videogame', 2300)
print(p1.valor)
print(p1.desconto(20))
p2 = Produto('Xbox S', 'Videogame', 3400)
print(p2.valor)
p3 = Produto('arroz', 'mercado', 15.50)
p3.peso = '5Kg'   # atributos dinâmicos, em tempo de execução
print(f'Produto: {p3.nome}, descrição: {p3.descricao}, valor: {p3.valor}, peso: {p3.peso}')


class Usuario:

    contador = 0

    @staticmethod
    def define():
        return "retorno sem cls"

    @classmethod    # métodos de classe
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)  # Atributos privados (__)
        Usuario.contador = self.__id

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user = Usuario('ana', 'ghiraldelli', 'ana@gmail.com', '12345')
Usuario.conta_usuarios()
