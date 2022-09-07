#DESAFIO - 025
#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.
n = str(input('Digite um nome completo: '))
print('É verdade que o nome {} tem "Silva" em algum lugar?'.format(n))
print('Silva' in n)
