#DESAFIO - 006:
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
# Poderia ser : n = float(input('Digite um número: ')) tranquilamente, porém, nos prenderemos aos inteiros aqui!
d = n * 2
t = n * 3
r = n ** (1/2)
print('Seu número é o {}!'.format(n))
print('Que tem como dobro o {}'.format(d))
print('E como triplo o {}'.format(t))
print('Além de sua raíz quadrada ser {:.2f}'.format(r))
