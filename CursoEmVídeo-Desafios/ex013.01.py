#DESAFIO - 013
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual é o salário do funcionário? [reais] '))
ns = s + ((15/100) * s)
print('De acordo com o reajuste salarial de 15% de aumento,', end=' ')
print('o salário que era {:.2f} reais, foi para {:.2f} reais!'.format(s, ns))
