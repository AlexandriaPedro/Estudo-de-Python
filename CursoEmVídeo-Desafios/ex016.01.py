#DESAFIO - 016
#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
#Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira como o 6.
from math import trunc
n = float(input('Digite um número real: '))
print('O número {} tem como parte inteira o {}!'.format(n, trunc(n)))
