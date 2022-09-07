#DESAFIO - 059
#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
r = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while r != 5:
    print('')
    print('''[1] para somar
[2] para multiplicar
[3] para escolher o maior número
[4] para digitar novos números
[5] para sair do programa''')
    r = int(input(('Qual opção desejas? ')))
    print('')
    if r == 1:
        print(' {} + {} = {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print(' {} x {} = {}'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            m = n1
        else:
            m = n2
        print('O maior número dentre os dois digitados é o {}!'.format(m))
    elif r == 4:
        n1 = int(input('Digite um novo primeiro valor: '))
        n2 = int(input('Digite um novo segundo valor: '))
    elif r == 5:
        print('Ok, encerrando o programa...')
    else:
        print('Você digitou uma opção inexistente, tente novamente!')
