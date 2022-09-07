#DESAFIO - 053
#Crie um programa que uma frase qualquer e diga se ela é um palindromo. Desconsiderando os espaços.
#Palindromo é uma frase que pode ser lida de frente pra trás e de trás pra frente.
#Ex: apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o bolo; anotaram a data da maratona.
fc = ''
f = str(input('Digite um frase sem acentuação: '))
f1 = f.lower().strip().split()
f1 = ''.join(f1).capitalize()
#print(f1)
for c in range(len(f1) - 1, -1, -1):
    fc = fc + (f1[c])
fc1 = fc.capitalize()
#print(fc1)
print('A frase digitada foi "{}",'.format(f1))
print('que lida ao contrário dá a frase "{}".'.format(fc1))
if f1 == fc1:
    print('Logo, a frase digitada É UM PALÍNDROMO!')
    print('Sendo palíndromo a frase que pode ser lida tanto')
    print('de frente pra trás, quanto de trás pra frente.')
else:
    print('Logo, a frase digitada NÃO É UM PALÍNDROMO!')
    print('Sendo palíndromo a frase que pode ser lida tanto')
    print('de frente pra trás, quanto de trás pra frente.')
