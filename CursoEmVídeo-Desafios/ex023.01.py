#DESAFIO - 023
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#      Unidade: 4
#      Dezena: 3
#      Centena: 8
#      Milhar: 1
n = str(input('Digite um número de 0 a 9999: '))
print('O número {} tem:'.format(n))
print('     {} unidade(s);'.format(n[-1]))
print('     {} dezena(s);'.format(n[-2]))
print('     {} centena(s);'.format(n[-3]))
print('     {} milhar.'.format(n[-4]))

#Programa mal feito!
#Programa só funciona bem, se para números pequenos colocarmos zeros para completarmos as 4 casas.