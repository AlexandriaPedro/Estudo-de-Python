#DESAFIO - 055
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
p = float(input('Quanto você pesa? [kg] '))
maior = p
menor = p
for c in range(0, 4):
    p1 = float(input('Quanto você pesa? [kg] '))
    if p1 > maior:
        maior = p1
    elif p1 < menor:
        menor = p1
print('Das 5 pessoas que digitaram seus pesos, pode-se afirmar que:')
print('O maior peso foi {:.1f}Kg e o menor peso foi {:.1f}Kg.'.format(maior, menor))
