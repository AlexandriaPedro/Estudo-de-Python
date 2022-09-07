#DESAFIO - 007
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite sua 1ª nota: '))
n2 = float(input('Digite sua 2ª nota: '))
m = (n1 + n2) / 2
print('Ou seja, sua nota média foi de {:.1f} pontos!'.format(m))
