#DESAFIO - 027
#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite um nome completo: '))
print('Dado o nome {} infere-se que:'.format(n))
n = n.split()
a = n[0]
b = n[-1]
print('O primeiro nome é: {};'.format(a))
print('O último nome é: {};'.format(b))
