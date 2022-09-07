f = 1
n = int(input('Digite um número inteiro qualquer: '))
if n == 0:
    print('O fatorial de 0 é 0.')
else:
    for c in range(n, 1, -1):
        f *= c
    print('O fatorial de {} é {}.'.format(n, f))
