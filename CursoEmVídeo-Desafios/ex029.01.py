#DESAFIO - 029
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
#que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limite.
n = int(input('Qual era a velocidade do carro: [Km/h] '))
if n > 80:
    d = (n - 80)
    m = d * 7
    print('A multa aplicada por ultrapassar {} Km do limte máximo da via,'.format(d))
    print('que é de 80 Km/h, corresponde a {:.2f} reais!'.format(m))
else:
    print('A velocidade de {} Km/h está dentro da faixa limite da via,'.format(n))
    print('que é de 80 Km/h. Sendo assim, o carro não é passível de multa!')
