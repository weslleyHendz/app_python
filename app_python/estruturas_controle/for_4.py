# for i in range(1, 10):
#     if == 5:
#         break
#     print(i)
# else:
#     print('Fim!')


# Dado 6 numeros entre 1 e 6
# For com range 1 a 6
# se for impar continue
# se o número for par e igual ao sorteado, imprimir 'ACERTOU' e depois chamar o break.
# se não chamar, chama o else

from random import randint

sortear_dado = randint(1, 7)
for x in range(1, 7):
    if x % 2 == 1:
        print('continuando')
        continue
    elif x % 2 == 0:
        if sortear_dado == x:
            print("ACERTOU. O número sorteado é: {}".format(sortear_dado))
            break
    else:
        print('você não acertou')
