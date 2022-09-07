#DESAFIO - 031
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
n = int(input('Qual é a distância da viagem que será feita? [Km] '))
if n > 200:
    p = n * 0.45
    print('Como a distância de sua viagem ultrapassa os 200 Km, será cobrado R$0.45 por Km.')
    print('Ou seja, o valor de sua passagem para fazer uma viagem de {} Km é de R${:.2f}!'.format(n, p))
else:
    p = n * 0.50
    print('Como a distância de sua viagem está dentro do limite de até 200 km, será cobrado R$0.50 por Km.')
    print('Ou seja, o valor de sua passagem para fazer uma viagem de {} Km é de R${:.2F}!'.format(n, p))
