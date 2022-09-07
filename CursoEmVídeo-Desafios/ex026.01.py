#DESAFIO - 026
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
n = str(input('Digite uma frase: '))
a = n.lower().count('a')
b = n.lower().find('a')
c = n.lower().rfind('a')
print('Dada a frase "{}", percebe-se que:'.format(n))
print('A letra "a" (+/-) aparece {} vezes;'.format(a))
print('A letra "a" (+/-) aparece a primeira vez na posição {};'.format(b))
print('A letra "a" (+/-) aparece a última vez na posição {}.'.format(c))
