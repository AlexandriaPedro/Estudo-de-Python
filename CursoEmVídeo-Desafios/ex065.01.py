#DESAFIO - 065
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre
#a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
#perguntar ao usuário se ele quer ou não continuar a digitar valores.
r = ''
g = 0
menor = 0
maior = 0
st = 0
m = 0
while r != 'n':
    n = int(input('Digite um número inteiro qualquer: '))
    if g == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    st += n
    g += 1
    r = str(input('Deseja continuar a digitar valores? [s/n] ')).lower().strip()
m = st / g
print('Dado os {} valores digitados, percebe-se quer:'.format(g))
print('O maior valor digitado foi o {};'.format(maior))
print('O menor valor digitado foi o {};'.format(menor))
print('A média entre os valores digitados foi {}.'.format(m))
