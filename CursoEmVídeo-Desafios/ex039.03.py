from datetime import date
atual = date.today().year
s = str(input('Qual o seu sexo? [M/F] '))
s = s.strip().lower()
if s == 'f':
    print('Você não precisa de alistamento!')
elif s == 'm':
    nasc = int(input('Qual seu ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Opção inválida, tente novamente.')