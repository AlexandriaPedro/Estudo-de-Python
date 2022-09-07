#DESAFIO - 020
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a = str(input('Digite o nome do 1° aluno: '))
b = str(input('Digite o nome do 2° aluno: '))
c = str(input('Digite o nome do 3° aluno: '))
d = str(input('Digite o nome do 4° aluno: '))
lista = [a, b, c, d]
print('A ordem dos sorteados são:', end=' ')
random.shuffle(lista)
print(lista)
