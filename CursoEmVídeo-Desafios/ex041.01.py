#DESAFIO - 041
#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM;
#Até 14 anos: INFANTIL; Até 19 anos: JUNIOR; Até 20 anos: SÊNIOR; Acima: MASTER.
from datetime import date
a_a = int(date.today().year)
a_n = int(input('Qual seu ano de nascimento? '))
d = abs(a_a - a_n)
print('Como você nasceu em {} e hoje estamos em {}, sua categoria é:'.format(a_n, a_a))
if d <= 9:
    print('MIRIM! Pois você vai ter até 9 anos de idade nesse ano.')
elif d <= 14:
    print('INFANTIL! Pois você vai ter 10 anos ou até 14 anos de idade nesse ano.')
elif d <= 19:
    print('JÚNIOR! Pois você vai ter 15 anos ou até 19 anos de idade nesse ano.')
elif d <= 20:
    print('SÊNIOR! Pois você vai ter 20 anos de idade nesse ano.')
elif d > 20:
    print('MASTER! Pois você vai ter mais de 20 anos nesse ano.')
