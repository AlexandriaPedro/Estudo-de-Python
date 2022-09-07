#DESAFIO - 017
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('sendo {} e {} os respectivos catetos,'.format(co, ca))
print('o comprimento da hipotenusa é {}!'.format(hip))
