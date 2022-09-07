#DESAFIO - 038
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, os dois são iguais.
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
print('Sendo o primeiro valor o {}, e o segundo o {}, percebe-se que:'.format(n1, n2))
if n2 > n1:
    print('O segundo valor é o maior valor digitado, sendo ele o número {}!'.format(n2))
elif n1 > n2:
    print('O primeito valor é o maior valor digitado, sendo ele o número {}!'.format(n1))
else:
    print('O primeiro e segundo valor são iguais, logo, não há valor maior entre {} e {}!'.format(n1, n2))
