#DESAFIO - 018
#Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, consseno e tangente desse ângulo.
import math
a = float(input('Digite o valor de um ângulo qualquer: '))
print('O ângulo de {:.2f}° tem:'.format(a))
print('O seno como {:.2f},'.format(math.sin(math.radians(a))))
print('O consseno como {:.2f},'.format(math.cos(math.radians(a))))
print('E a tangente como {:.2f}!'.format(math.tan(math.radians(a))))
