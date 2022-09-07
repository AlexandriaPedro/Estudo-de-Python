#DESAFIO - 005:
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
s = n + 1
a = n - 1
print('Seu número foi o {}!'.format(n))
print('Que tem como sucessor o {}'.format(s))
print('E como antecessor o {}'.format(a))
