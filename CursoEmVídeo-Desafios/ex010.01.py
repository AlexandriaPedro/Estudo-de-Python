#DESAFIO - 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere: US$1.00=R$3.27
n = float(input('Quantos reais você tem na carteira: '))
d = n / 3.27
print('Com o valor de {:.2f} reais, você pode comprar {:.2f} dólares!'.format(n, d))
