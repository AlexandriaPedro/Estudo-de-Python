#DESAFIO - 061
#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
#os 10 primeiros termos da progressão usando a estrutura while.
c = -1
p = int(input('Digite o Primeiro Termo da P.A: '))
r = int(input('Digite o Razão da P.A: '))
while c != 9:
    c += 1
    print('{}'.format(p + r * c))
