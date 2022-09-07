#DESAFIO - 035
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
n1 = float(input('Diga o tamanho da primeira reta: '))
n2 = float(input('Diga o tamanho da segunda reta: '))
n3 = float(input('Diga o tamanho da terceira reta: '))
print('Sendo o tamanho das retas, respectivamente, {}, {} e {},'.format(n1, n2, n3))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('pode-se dizer que, essas retas podem formar um triângulo!')
else:
    print('pode-se dizer que, essas retas não podem formar um triângulo!')
