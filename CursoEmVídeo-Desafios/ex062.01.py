#DESAFIO - 062
#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.
termos = -1
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
    if c == décimo:
        último_antes = c
while termos != 0:
    termos = int(input('\nDeseja colocar mais alguns termos (Quantos): '))
    if termos != 0:
        último_depois = último_antes + termos * razão
        for c in range(último_antes + razão, último_depois + razão, razão):
            print('{} '.format(c), end='-> ')
            if c == último_depois:
                último_antes = último_depois
print('ACABOU')
