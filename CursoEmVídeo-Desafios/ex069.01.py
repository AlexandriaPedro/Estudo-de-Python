#DESAFIO - 069
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
#deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) Quantas pessoas tem mais
#de 18 anos; B) Quantos homens foram cadastrados; C) Quantas mulheres tem menos de 20 anos.
total_mais_18 = quant_h = quant_m_menos_20 = 0

while True:
    while True:
        sexo = str(input("Diga lá, seu sexo: (M ou H) "))
        sexo = sexo.capitalize().strip()

        if sexo != 'M' and sexo != 'H':
            print("Dê um dos dois, meu fi. Só pode ser ou M ou H, então bora!")
            print("\n")
        else:
            break
    
    idade = int(input("Diga lá agora, qual sua idade, meu fi? "))

    if idade > 18:
        total_mais_18 += 1
    if sexo == 'H':
        quant_h += 1
    if sexo == 'M' and idade < 20:
        quant_m_menos_20 += 1

    print("\n")

    while True:
        resp = str(input("Quer cadastrar mais alguem? (S ou N)"))
        resp = resp.capitalize().strip()
        
        if resp != 'S' and resp != 'N':
            print("Dê um dos dois, meu fi. Só pode ser ou M ou H, então bora!")
            print("\n")
        else:
            break
    
    if resp == 'N':
        print("Pois bem, então te mostrarei os resultados até então...")
        print(f"Quantidade de pessoas maiores de 18 anos: {total_mais_18}")
        print(f"Quantidade total de homens : {quant_h}")
        print(f"Quantidade de mulheres com menos de 20 anos: {quant_m_menos_20}")
        break
