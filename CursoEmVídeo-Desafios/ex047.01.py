#DESAFIO - 047
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 a 50.
print('Os números pares entre 1 a 50 são:')
for c in range(1, 51):
    if c % 2 == 0:
        print('{}; '.format(c), end='')
