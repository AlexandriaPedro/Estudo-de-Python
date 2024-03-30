#DESAFIO - 070
#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
#se o usuário vai continuar. No final, mostre: A) Qual é o total gasto na compra;
#B) Quantos produtos custam mais de R$1000; C) Qual é o nome do produto mais barato.
total_gasto = quanto_mais_de_1000 = preco_produto_barato = contador = 0
qual_mais_barato = ''

while True:
    nome_produto = str(input("Me fale o nome do produto: "))
    preco_produto = float(input("Me fale o preço do produto: "))

    contador += 1

    total_gasto += preco_produto

    if preco_produto > 1000:
        quanto_mais_de_1000 += 1
    
    if contador == 1:
        qual_mais_barato = nome_produto
        preco_produto_barato = preco_produto
    elif preco_produto < preco_produto_barato:
        qual_mais_barato = nome_produto
        preco_produto_barato = preco_produto
    
    while True:
        resp = str(input("Quer continuar a registrar produtos? (S ou N) "))
        resp = resp.capitalize().strip()

        if resp != 'N' and resp != 'S':
            print("Me ajuda ai né, responde algo que existe mlk! É ou S ou N, pô")
            print("Tenta de novo.")
            print("\n")
        else:
            break

    qual_mais_barato = qual_mais_barato.capitalize().strip()
    
    if resp == 'N':
        print("Beleza, então vamos te dar o resultado da sua compra...")
        print(f"Bem, o tal gasto foi de {total_gasto:.2f} reais")
        print(f"{quanto_mais_de_1000} produtos custaram mais de 1000 reais")
        print(f"E o produto de nome {qual_mais_barato} foi o produto mais barato que você comprou,")
        print(f"valendo apenas {preco_produto_barato:.2f} reais.")
        break