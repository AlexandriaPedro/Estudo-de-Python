from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}'.format(num, raiz))
print('ou igual a {} se arredondarmos pra cima, e {} se arredondarmos pra baixo'.format(ceil(raiz), floor(raiz)))
