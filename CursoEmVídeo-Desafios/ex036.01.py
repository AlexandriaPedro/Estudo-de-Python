#DESAFIO - 036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
#ela não pode exceder 30% do salário ou então o empréstimo será negado.
v = float(input('Qual é o valor da casa? R$'))
s = float(input('De quanto é o seu salário? R$'))
a = float(input('Pretente pagar a casa em quantos anos? '))
p = v / (12 * a)
print('Sendo o valor das parcelas mensais R${:.2f},'.format(p))
print('e sendo seu salário de R${}:'.format(s))
if p > 30/100 * s:
    print('Será impossível comprar a casa, pois o valor')
    print('das parcelas mensais ultrapassa 30% do seu salário!')
elif p <= 30/100 * s:
    print('Será possível comprar a casa, pois o valor das')
    print('parcelas mensais equivalem a 30% ou menos de seu salário!')
