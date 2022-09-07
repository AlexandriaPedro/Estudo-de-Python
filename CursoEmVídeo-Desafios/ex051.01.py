#DESAFIO - 051
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
for c in range(0, 10):
    print('{}'.format(p + (r * c)))
