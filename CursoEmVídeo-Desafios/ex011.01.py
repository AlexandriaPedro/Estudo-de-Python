#DESAFIO - 011
#Faça um programa que leia a largura e a altura de uma parede em metros.Calcule sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinha pinta uma área de 2m^2.
l = float(input('Digite a largura da parede: [metros] '))
h = float(input('Digite a altura da parede: [metros] '))
a = l * h
t = a / 2
print('Se a parede tem {:.2f} m^2 de área,'.format(a))
print('você vai precisar de {:.2f} litros \nde tinta para pintá-la'.format(t))
