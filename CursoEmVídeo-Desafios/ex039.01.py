#DESAFIO - 039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se
#alistar ao serviço militar; Se é a hora de se alistar; Se já passou do tempo de alistamento. Seu programa também
#deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date, datetime
data_hoje = date.today()
data_hoje_str = data_hoje.strftime('%d/%m/%Y')
dia = str(input('Em que dia você nasceu? '))
mes = str(input('Em que mês você nasceu? '))
ano = str(input('Em que ano você nasceu? '))
data_nasc_str = '{:0>2}'.format(dia) + '/' + '{:0>2}'.format(mes) + '/' + ano
data_nasc = datetime.strptime(data_nasc_str, '%d/%m/%Y').date()
subtraction_dias = abs((data_hoje - data_nasc).days)
print('Se você nasceu em {} e hoje é {}, então...'.format(data_nasc_str, data_hoje_str))
if subtraction_dias > 19 * 365:
    print('Já passou do tempo de você se alistar, pois além de você já ter feito 19 anos,')
    print('também se passou {} dia(s) desde que você fez essa idade!'.format(subtraction_dias - (19 * 365)))
elif subtraction_dias == 19 * 365:
    print('Já passou do tempo de você se alistar, pois é exatamente hoje que você faz 19 anos!')
    print('Aliás, meus parabéns amiguxo! Tenha um ótimo dia e que o amor esteja contigo sempre!')
elif subtraction_dias < 19 * 365 and subtraction_dias > 18 * 365:
    print('Você está na faixa de idade onde se pode alistar,')
    print('sendo que já se passou {} dia(s) desde que você fez 18 anos,'.format(subtraction_dias - (18 * 365)))
    print('e falta {} dia(s) para você fazer 19 anos!'.format((19 * 365) - subtraction_dias))
elif subtraction_dias == 18 * 365:
    print('A partir de hoje você já pode se alistar, pois é exatamente hoje que você faz 18 anos!')
    print('Aliás, meus parabéns, amiguxo! Tenha um ótimo dia e que o amor esteja contigo sempre!')
elif subtraction_dias < 18 * 365:
    print('Ainda não chegou o tempo de você se alistar, pois você ainda não fez 18 anos,')
    print('até por que falta {} dia(s) para você atingir essa idade!'.format((18 * 365) - subtraction_dias))
