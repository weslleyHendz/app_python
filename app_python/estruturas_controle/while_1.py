# while True:
#     print('Vai demorar muito
#     ')

from random import randint

numero_informado = int(input('Informe um número de 0 a 9: '))
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print('Numero secreto {} foi encontrado!'.format(numero_secreto))
