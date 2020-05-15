produto = {'nome' : 'Caneta chic', 'preco': 14.99,
           'importada': True, 'estoque' :754}

for chav in produto:
    print(chav)

for valo in produto.values():
    print(valo)

for chav, valo in produto.items():
    print(chav, '=', valo)