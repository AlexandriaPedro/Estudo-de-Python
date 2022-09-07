#DESAFIO - 040
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida: Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO;
#Média 7.0 ou superior: APROVADO.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sendo sua média {}, percebe-se que...'.format(m))
if m >= 7.0:
    print('Você está APROVADO, visto que sua média foi maior ou igual a 7!')
elif m >= 5.0 and m < 7.0:
    print('Você está de RECUPERAÇÃO, visto que sua média está entre 5.0 e 6.9!')
elif m < 5.0:
    print('Você está REPROVADO, visto que sua média é menor que 5.0!')
