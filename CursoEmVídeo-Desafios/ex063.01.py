#DESAFIO - 063
#Escreva um programa que leia um número n inteiro qualquer e mostre
#na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 -> 1 -> 2 -> 4 -> 5 -> 8
n = int(input('Digite um número inteiro qualquer: '))
a = 1
m = 1
p = 2
s = 0
print('A quantidade de termos na sequência de Fibonacci dada é:')
if n == 0:
    print('Ok, nenhum termo da sequência será mostrada.')
elif n == 1:
    print('0 ->')
else:
    print('0 -> 1 ', end='')
    while s != n - 2:
        print('-> {} '.format(m), end='')
        a = m
        m = p
        p = m + a
        s = s + 1