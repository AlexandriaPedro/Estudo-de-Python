f = 1
n = int(input('Digite um número inteiro qualquer: '))
c = n
if n == 0:
    print('O fatorial de 0 é 0.')
else:
    while c != 1:
        f *= c
        c -= 1
    print('O fatorial de {} é {}.'.format(n, f))
