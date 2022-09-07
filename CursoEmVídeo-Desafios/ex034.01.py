#DESAFIO - 034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
#superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
n = float(input('Qual o salário do funcionário? '))
if n > 1250.00:
    nv = n + (10/100 * n)
    print('Como o salário é maior que R$1,250.00, o aumento salarial será de 10%!')
    print('Fazendo assim, que o novo salário seja R${}!'.format(nv))
else:
    nv = n + (15/100 * n)
    print('Como o salário é menor ou igual a R$1,250.00, o aumento salarial será de 15%!')
    print('Fazendo assim, que o novo salário seja R${}!'.format(nv))
