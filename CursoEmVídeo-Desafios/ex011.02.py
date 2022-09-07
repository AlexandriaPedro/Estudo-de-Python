larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {:.2f}x{:.2f},'.format(larg, alt))
print('e sua área é de {}m².'.format(área))
tinta = área / 2
print('Logo, para pintar essa parede, ')
print('você precisará de {}l de tinta.'.format(tinta))
