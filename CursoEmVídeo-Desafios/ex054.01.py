#DESAFIO - 054
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
#ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ah = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    ap = int(input('Qual seu ano de nascimento? '))
    if ah - ap >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Das 7 pessoas que deram seus anos de nascimento:')
print('{} são maiores de idade e {} são menores de idade.'.format(maior, menor))