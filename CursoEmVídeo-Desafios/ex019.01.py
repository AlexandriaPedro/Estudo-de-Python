#DESAFIO - 019
#Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrendo o nome do escolhido.
from random import choice
a = str(input('Qual nome do 1° aluno: '))
b = str(input('Qual nome do 2° aluno: '))
c = str(input('Qual nome do 3° aluno: '))
d = str(input('Qual nome do 4° aluno: '))
lista = a, b, c, d
print('O nome sorteado foi: {}!'.format(choice(lista)))
