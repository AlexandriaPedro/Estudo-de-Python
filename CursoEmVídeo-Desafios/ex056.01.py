#DESAFIO - 056
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres têm menos de 20 anos.
it = 0
ihv = 0
mm20 = 0
hv = ''
for c in range(0, 4):
    n = str(input('Qual é seu nome? ')).strip()
    i = int(input('Qual é sua idade? '))
    s = str(input('Qual é o seu sexo? [M/F] ')).lower().strip()
    if s == 'm':
        if i > ihv:
            ihv = i
            hv = n
    elif s == 'f':
        if i < 20:
            mm20 += 1
    it += i
mit = it / 4
print('')
print('De acordo com os dados digitados, percebe-se que:')
print('A média de idade total foi de {:.2f} anos;'.format(mit))
print('O homem mais velho foi o {} com {} anos;'.format(hv, ihv))
print('E houve {} mulheres com idade abaixo de 20 anos.'.format(mm20))
