#DESAFIO - 032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
n = int(input('Digite um ano qualquer: '))
if n % 4 == 0:
    print('O ano {} é um ano BISSEXTO!'.format(n))
else:
    print('O ano {} não é BISSEXTO!'.format(n))
