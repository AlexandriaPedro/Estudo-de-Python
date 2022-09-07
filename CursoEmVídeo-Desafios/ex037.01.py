#DESAFIO - 037
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
#de conversão: 1 para binário; 2 para octal; 3 para hexadecimal.
n = int(input('Digite um número inteiro qualquer: '))
print('Digite [1] para transformá-lo em binário;')
print('Digite [2] para transformá-lo em octal;')
print('Digite [3] para transformá-lo em hexadecimal;')
r = int(input('Digite a opção pretendida: '))
if r == 1:
    print('O número {} em binário é {}!'.format(n, bin(n)))
elif r == 2:
    print('O número {} em octal é {}!'.format(n, oct(n)))
elif r == 3:
    print('O número {} em hexadecimal é {}!'.format(n, hex(n)))
else:
    print('Opção inexistente, reinicie o programa e tente uma opção válida!')
