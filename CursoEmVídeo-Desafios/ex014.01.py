#DESAFIO - 014
#Escreva um programa que converta uma temperatura digitando em graus Celcius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em °C: '))
f = (c * 1.8) + 32
print('A temperatura de {:.1F}°C corresponde a {:.1F}ºF'.format(c, f))
