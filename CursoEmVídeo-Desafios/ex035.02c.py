print('\033[33m-=-\033[m' * 20)
print('\033[1;33m                 Analisador de Triângulos\033[m')
print('\033[33m-=-\033[m' * 20)
r1 = float(input('\033[97mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\33[1;32mOs segmentos acima PODEM FORMAR triângulo!')
else:
    print('\33[1;31mOs segmentos acima NÃO PODEM FORMAR triângulos!')
