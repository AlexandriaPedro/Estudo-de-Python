#DESAFIO - 067
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
#pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('-=' * 50)
print(f'{" T A B U A D A ":~^100}')
print('-=' * 50)
while True:
    n = int(input('Digite um número para fazermos a tabuada dele ou digite um número negativo para encerrar: '))
    print('¨' * 100)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')
    print('¨' * 100)
print(f'{" Encerrando o programa. Obrigado! Volte sempre! ":~^100}')
