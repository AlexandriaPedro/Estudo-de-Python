import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raíz quadrada de {} é igual a {:.2f}'.format(num, raiz))
print('ou igual a {} se arredondarmos pra baixo, e {} se arredondarmos pra cima'.format(math.floor(raiz), math.ceil(raiz)))
