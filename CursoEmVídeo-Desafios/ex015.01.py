#DESAFIO - 015
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0.15 por Km rodado.
qkm = float(input('Quantos Km o carro alugado andou? '))
qd = int(input('E ele foi alugado por quantos dias? '))
p = 60 * qd + 0.15 * qkm
print('Sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado,')
print('o preço que deve ser pago pelo aluguel é de R${:.2F}!'.format(p))
