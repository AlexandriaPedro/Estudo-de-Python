#DESAFIO - 044
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento: À vista dinheiro/cheque: 10% de desconto; À vista no cartão: 5% de desconto;
#Em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.
v = float(input('Digite o valor do produto: R$'))
print('Escolha uma das opções de pagamento para realizar a compra:')
r = int(input("""    
    [1] À vista dinheiro/cheque
    [2] À vista no cartão
    [3] Em até 2x no cartão
    [4] Em 3x ou mais no cartão
         
Qual opção desejas? """))
if r == 1:
    nv = v - ((10 / 100) * v)
    print('A opção [1] dá 10% de desconto no valor do produto,')
    print('ou seja, o produto que valia R${:.2f} agora vale R${:.2f}!'.format(v, nv))
elif r == 2:
    nv = v - ((5 / 100) * v)
    print('A opção [2] dá 5% de desconto no valor do produto,')
    print('ou seja, o produto que valia R${:.2f} agora vale R${:.2f}!'.format(v, nv))
elif r == 3:
    nv = v
    print('A opção [3] deixa o produto com o mesmo valor,')
    print('ou seja, o produto que valia R${:.2f} continua valendo R${:.2f}!'.format(v, nv))
elif r == 4:
    nv = v + ((20 / 100) * v)
    print('A opção [4] dá 20% de juros no valor do produto,')
    print('ou seja, o produto que valia R${:.2f} agora vale R${:.2f}!'.format(v, nv))
else:
    print('A opção selecionada não existe. Por favor, tente uma válida!')
