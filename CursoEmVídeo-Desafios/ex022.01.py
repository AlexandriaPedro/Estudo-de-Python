#DESAFIO - 022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome.

nome = str(input('Escreva um nome completo: '))
print('O nome todo em maiúsculo:', nome.upper())
print('o nome todo em minúsculo:', nome.lower())
nome = nome.split()
print('Quantas LETRAS tem ao todo:', len(''.join(nome)))
print('Quantas letras tem o primeiro nome:', len(nome[0]))
