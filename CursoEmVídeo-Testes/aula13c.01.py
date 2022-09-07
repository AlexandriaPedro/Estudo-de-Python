s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #Isso de "+=" é igual a: s = s + n
print('O somatório de todos os valores foi {}!'.format(s))

#Ou seja, se você quer que um número receba ele mesmo, invés de colocar ele igual a ele (ex: s = s + n),
#coloque ele mais igual e segue o jogo (ex: s += n) ...
