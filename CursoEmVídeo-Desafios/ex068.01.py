#DESAFIO - 068
#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
#jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random

print('-='*51)
print(f'{" Í M P A R  ou  P A R ":~^102}')
print('-='*51)

vitorias = soma = 0
comp = ''

while True:
    resposta1 = str(input('escolha entre ímpar ou par: '))
    resposta1 = resposta1.capitalize().strip()

    if resposta1 == 'Impar' or resposta1 == 'Ímpar':
        comp = 'Par'
    if resposta1 == 'Par' :
        comp = 'Ímpar'
    
    respcomp = random.randint(0, 10)

    resposta2 = int(input('Diga lá! Qual número vai jogar? '))
    print("\n")

    soma = respcomp + resposta2

    if (soma % 2 == 0) and (comp == "Par"):
        print(f"Como o computador escolheu o número {respcomp}, então a soma deu {soma} e o computador venceu, porque {soma} é Par!")
        print("Tente de novo, depois!")
        print("\n")
        print(f"Saldo de vitórias: {vitorias}")
        print('-='*51)
        break
    elif (soma % 2 == 0) and (comp == "Ímpar"):
        print(f"Como o computador escolheu o número {respcomp}, então a soma deu {soma} e o Você venceu, porque {soma} é Par!")
        print("Muito Massa!")
        print("\n")
        print("Bora pra próxima :p")
        print('-='*51)
        vitorias += 1
    elif (soma % 2 != 0) and (comp == "Ímpar"):
        print(f"Como o computador escolheu o número {respcomp}, então a soma deu {soma} e o computador venceu, porque {soma} é ímpar!")
        print("Tente de novo, depois!")
        print("\n")
        print(f"Saldo de vitórias: {vitorias}")
        print('-='*51)
        break
    elif (soma % 2 != 0) and (comp == "Par"):
        print(f"Como o computador escolheu o número {respcomp}, então a soma deu {soma} e o Você venceu, porque {soma} é Ímpar!")
        print("Muito Massa!")
        print("\n")
        print("Bora pra próxima :p")
        print('-='*51)
        vitorias += 1
