#DESAFIO - 048
#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
#e que se encontram no intervalo de 1 até 500.
s = 0
print('A soma de todos os números ímpares e que são múltiplos de três é: ')
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        print(' {:0>3}'.format(c))
        print('+')
        s += c #Isso é a mesma coisa que escrever: "s = s + c"
print(' 000')
print('--------')
print('=', s)