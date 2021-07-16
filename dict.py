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
