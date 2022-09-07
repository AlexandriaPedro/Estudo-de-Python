s = ' '
while s not in 'HmFm':
    s = str(input('Qual seu sexo? [H/F] ')).upper()
    if s not in 'HmFm':
        print('você digitou {}, e isso não é um sexo válido, tente novamente!'.format(s))
