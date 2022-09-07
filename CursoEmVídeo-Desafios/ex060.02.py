f = 1
c = -1
n = int(input('Digite um número inteiro: '))
print('Abaixo é a conta de seu fatorial...')
print('{}! = {} '.format(n, n), end='')
while c != 1:
    for c in range(n - 1, 0, -1):
        print('x {} '.format(c), end='')
    for c in range(n, 0, -1):
        f *= c
print('= {}'.format(f))
