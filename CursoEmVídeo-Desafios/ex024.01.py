#DESAFIO - 024
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
n = str(input('Qual nome da cidade? '))
print('É verdade que a cidade {} começa com "Santo"?'.format(n))
n = n.split()
print('Santo' in n[0][:5])
