#DESAFIO - 042
#Refaça o DESAFIO - 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: Todos os lados iguais; Isósceles: Dois lados iguais; Escaleno: Todos os lados diferentes.
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses valores de lado podem formar um triângulo possível? SIM!')
    print('Entretanto, esse triângulo possível...')
    if l1 == l2 and l2 == l3:
        print('É Equilátero? SIM!')
    else:
        print('É Equilátero? NÃO!')
    if (l1 == l2 and l1 != l3) or (l2 == l3 and l2 != l1) or (l3 == l1 and l3 != l2):
        print('É Isósceles? SIM!')
    else:
        print('É Isósceles? NÃO!')
    if l1 != l2 and l2 != l3 and l3 != l1:
        print('É Escaleno? SIM!')
    else:
        print('É Escaleno? NÃO!')
else:
    print('Esses valores de lado podem formar um triângulo possível? NÃO!')
