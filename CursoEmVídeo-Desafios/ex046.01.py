#DESAFIO - 046
#Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos de artifício.
#Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('-=' * 11)
print('CONTAGEM DOS FOGOS')
print('-=' * 11)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('')
print('!FOGOS!')
