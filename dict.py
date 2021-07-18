"""
Módulos Collections
- Counter (tranformar em "dicionário")
- defaultdict (criar chaves no dict)
- ordereddict (ordenar valores no dict)
- namedtuple (criamos um dado com um nome e parâmetro)
- deque (transforma qualquer dado em lista)
"""
from collections import Counter
lista = [1, 1, 1, 2, 2, 2, 2, 4, 6, 67, 45, 3, 3, 3, 45, 6, 6, 6, 7]
res = Counter(lista)
print(res)
print(Counter('Ana paula'))

# Coleções do tipo chave/valor
# em outras linguagens são chamados de mapas
# não são indexados
countries = dict(br="Brazil", pt="Portugal", eua="United States")
print(countries)
print(type(countries))

countries = {'br': "Brazil", 'pt': "Portugal", 'eua': "United States"}
print(countries)
print(type(countries))
print('br' in countries)

for chave in countries.keys():
    print(chave)

for valor in countries.values():
    print(valor)

# fromkeys recebe dois parametros: iteravel e valor
user = {}.fromkeys(['name', 'email', 'profile', 'points'], 'uncharted')
print(user)
novo = {}.fromkeys(range(1, 11), 'novo')
print(novo)

# Acessar elementos
print(countries.get('br'))

country = countries.get('ru', 'dont find')

russia = countries.get('ru')
if russia:
    print('found the country')
else:
    print("didn't find the country")

# tupla como chave
localities = {
    (12.5567, 3.65788): 'office',
    (434.67, 1.543): 'company',
}
print(localities)

# add
receita = {'jan': 100, 'fev': 200, 'mar': 300, 'abr': 400}
print(receita)
receita['mai'] = 500
print(receita)
receita.update({'fev': 250})
print(receita)
# remove
receita.pop('mai')  # del pode ser usado
print(receita)

# exemplos
carrinho = []
produto1 = {'nome:': 'Playstation', 'quantidade:': 1, 'preço:': 2500.0}
produto2 = {'nome:': 'Stardew Valley', 'quantidade:': 1, 'preço:': 25.0}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

"""
Sets - conjuntos
- representados por chaves {}
- não tem valores duplicados
"""
s = {23, 44, 56, 1, 2, 65, 4, 4, 1}
print(s)
print(type(s))
print(len(set(s)))  # não existe repetição

# revisando coleções
lista = [1, 99, 76, 45, 45, 3, 1]
print(f'Lista: {lista} com {len(lista)} elementos')
tupla = 1, 99, 76, 45, 45, 3, 1
print(f'Tupla: {tupla} com {len(tupla)} elementos')
dicionario = {}.fromkeys([1, 99, 76, 45, 45, 3, 1], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
sets = {1, 99, 76, 45, 45, 3, 1}
print(f'Conjuntos: {sets} com {len(sets)} elementos')
