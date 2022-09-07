#DESAFIO - 050
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o. Tipo, ele não vai ir pra soma, entendeu?
s = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n #Isso é a mesma coisa que escrever: "s = s + n"
print('A soma dos números pares digitados é {}!'.format(s))
