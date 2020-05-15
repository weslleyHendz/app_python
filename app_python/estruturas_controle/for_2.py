palavra = 'letsdobetter'
for letr in palavra:
    print(letr, end=',')
print('\nfim ')
aprovados= ['weslley', 'diandra', 'teca']
for name in aprovados:
    print (name, end='\n')

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)
