#DESAFIO - 057
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'H' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Qual seu sexo? [H/F] ')).upper()
while s not in 'HmFm':
    print('você digitou {}, e isso não é um sexo válido, tente novamente'.format(s))
    s = str(input('Qual seu sexo? [H/F] ')).upper()
