#DESAFIO - 028
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador. Obs: O programa deverá escrever na tela se
#o usuário venceu ou perdeu.
from random import randint
n = randint(0, 5)
r = int(input('Digite um número entre 0 e 5: '))
if r == n:
    print('Parabéns, o número sorteado foi {},'.format(n))
    print('e você acertou em cheio!')
else:
    print('Pô, o número sorteado foi {} e não {},'.format(n, r))
    print('você errou, infelizmente, amiguxo!')
print('{:-^36}'.format('FIM'))
