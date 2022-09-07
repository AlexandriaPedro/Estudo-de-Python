#DESAFIO - 052
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
f = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        f += 1
if f == 2:
    print('{} é um número PRIMO!'.format(n))
    print('Pois, é divisível apenas {} vezes.'.format(f))
elif f == 1:
    print('{} NÃO é um número PRIMO!'.format(n))
    print('Pois, é divisível apenas {} vez'.format(f))
    print('e não 2 vezes como um número primo!')
else:
    print('{} NÃO é um número PRIMO!'.format(n))
    print('Pois, é divisível {} vezes'.format(f))
    print('e não 2 vezes como um número primo!')
