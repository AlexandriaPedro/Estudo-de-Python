#DESAFIO - 008
#Escreva um programa que leia um valor em metros e o exiba convertidos em centímetros e milímetros.
v = float(input('Digite um valor: [metros] '))
c = v * 100
m = v * 1000
print('Pois bem, {:.2f} metros são {:.1f} centímetros'.format(v,c))
print('E são também {:.0f} milímetros'.format(m))
