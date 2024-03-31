#DESAFIO - 071
#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
#qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada
#valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

#ERREI O JEITO DO GUANABARA TÁ MAIS CERTO!

print("-=" * 52)
print(f'{"C A I X A   E L E T R Ô N I C O":^104}')
print("-=" * 52)

quant_50 = quant_20 = quant_10 = quant_1 = 0

valor = int(input("Falaaaa Mickey, quer tirar qual valor do caixa hoje? "))

resto = valor

while True:
    if resto >= 50:
        resto -= 50
        quant_50 += 1
    if resto >= 20:
        resto -= 20
        quant_20 += 1
    if resto >= 10:
        resto -= 10
        quant_10 += 1
    if resto >= 1:
        resto -= 1
        quant_1 += 1
    if resto == 0:
        break

print("\n")
print(f"Dado ao valor que nos foi solicitado, ou seja {valor:.2f} reais,")
print("Você receberá a seguinte quantidade de notas:")
print(f"{quant_50} de 50 reais")
print(f"{quant_20} de 20 reais")
print(f"{quant_10} de 10 reais")
print(f"{quant_1} de 1 real")
