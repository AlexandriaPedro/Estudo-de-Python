#DESAFIO - 012
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: [reais] '))
np = p - ((5/100) * p)
print('Com o desconto de 5% sobre o valor de {:.2f} reais'.format(p))
print('O produto sai por apenas {:.2f}! IMPERDÍVEL!'.format(np))
