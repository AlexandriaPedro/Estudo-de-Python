#DESAFIO - 049
#Refaça o DESAFIO - 009, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando o laço for.
print('{:=^60}'.format(' TABUADA '))
num = int(input('Digite um número inteiro para fazermos a tabuada dele: '))
print('-' * 60)
for c in range(1, 11):
    print(' {} X {:>2} = {}'.format(num, c, num * c))
print('-' * 60)
