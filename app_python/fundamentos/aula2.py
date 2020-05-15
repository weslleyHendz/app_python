a = int (input('Entre com o Primeiro valor: '))
b = int (input('Entre com o Segundo valor: '))
print(type(a))
a = 10
b = 6
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao= a/b
resto= a%b
resultado = ('Soma: {}. \nSubtração {}'
      '\nMultiplicação: {}'
      '\nDivisão: {}'
      '\nResto: {}'.format (soma, subtracao, multiplicacao, resto, divisao))

print(resultado)
# x= '1'
# soma2= int(x)+1
# print(soma2)