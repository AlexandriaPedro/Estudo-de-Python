#DESAFIO - 058
#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
#vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
r = -1
t = 1
m = randint(0, 10)
print('Pensei em um número, tente acertar qual é!')
while r != m:
    r = int(input(('Quê número cê acha que eu pensei? ')))
    if r == m:
        print('Parabéns, você acertou!')
        print('Eu pensei no {} e você digitou o {}!'.format(m, r))
        print('E você precisou de {} tentativas pra acertar!'.format(t))
    else:
        t += 1
        print('Você errou infelizmente... Mas vamos lá, tente de novo!')
