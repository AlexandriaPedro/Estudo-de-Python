#DESAFIO - 043
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu
#status, de acordo com a tabela abaixo: Abaixo de 18.5: Abaixo do peso; Entre 18.5 e 25:
#Peso ideal; 25 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade mórbida.
p = float(input('Digite seu peso: [Kg] '))
a = float(input('Digite sua altura: [m] '))
i = p / (a ** 2)
i = round(i, 1)
print('Sendo seu peso, {:.1f}Kg, e sua altura, {:.2f}m, seu IMC é igual a {:.1f}!'.format(p, a, i))
print("E de acordo com a tabela de IMC's, seu estado é de...")
if i < 18.5:
    print('ABAIXO DO PESO! Pois seu IMC está abaixo de 18.5.')
elif i >= 18.5 and i < 25:
    print('PESO IDEAL! Pois seu IMC está entre 18.5 e 25, sendo menor que 25.')
elif i >= 25 and i < 30:
    print('SOBREPESO! Pois seu IMC está entre 25 e 30, sendo menor que 30.')
elif i >= 30 and i <= 40:
    print('OBESIDADE! Pois seu IMC está entre 30 e 40.')
elif i > 40:
    print('OBESIDADE MÓRBIDA! Pois seu IMC está acima de 40.')
