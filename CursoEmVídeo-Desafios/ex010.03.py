real = float(input('Quanto dinheiro você tem na carteira? R$'))
dólar = real / 5.33
euro = real / 6.10
libra = real / 7.20
iene = real * 21.64
rupia = real * 14.03
pesoa = real * 19.77
print('Com R${:.2f} você pode comprar:'.format(real))
print('{:.2f} dólares'.format(dólar))
print('{:.2f} euros'.format(euro))
print('{:.2f} libras'.format(libra))
print('{:.0f} ienes'. format(iene))
print('{:.0f} rupias'.format(rupia))
print('{:.0f} pesos argentinos'.format(pesoa))
