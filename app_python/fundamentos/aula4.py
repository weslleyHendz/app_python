while (owner.isAlive()){
    owner.eat();
    owner.sleep();
    owner.code();
}

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota Invalida. Entre com a nota correta: '))


# a = 0
# while a <10:
#     print(a)
#     a += 1
## Números primos
# a = int(input('Entre com um valor: '))
#
# for num in range(a+1):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div ==2:
#         print(num)



# a = int(input('Entre com o número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div ==2:
#     print('número {} é primo'.format(a))
#
# else:
#     print('número {} não é primo'.format(a))
