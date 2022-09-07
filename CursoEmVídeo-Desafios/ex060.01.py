#DESAFIO - 060
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
f = 1
n = int(input('Digite um número inteiro qualquer: '))
print('Abaixo é a conta do seu fatorial...')
print('{}! = {}'.format(n, n), end='')
for c in range(n - 1, 0, -1):
    print(' x {}'.format(c), end='')
for c in range(n, 0, -1):
    f *= c
if n == 0:
    print(' = 0')
else:
    print(' = {}'.format(f))
