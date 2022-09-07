#DESAFIO - 045
#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
b = ['pedra', 'papel', 'tesoura']
rb = choice(b)
print('Vamos jogar Jokenpô!')
print('Já escolhi o que vou jogar, agora é sua vez.')
re = str(input('Você escolhe: Pedra, Papel ou Tesoura? Digite ->  '))
re = re.lower().strip().split()
re = ''.join(re)
if rb == 'pedra' and re == 'pedra':
    print('Uai, eu joguei {} e você jogou {} também!'.format(rb, re))
    print('Empatamos, droga!')
elif rb == 'pedra' and re == 'papel':
    print('Eu joguei {} e você jogou {}, logo...'.format(rb, re))
    print('Você venceu, Grrr!')
elif rb == 'pedra' and re == 'tesoura':
    print('Eu joguei {} e você jogou {}, logo...'.format(rb, re))
    print('Eu venci, yeah!')
elif rb == 'papel' and re == 'papel':
    print('Uai, eu joguei {} e você jogou {} também!'.format(rb, re))
    print('Empatamos, droga!')
elif rb == 'papel' and re == 'pedra':
    print('Eu joguei {} e você jogou {}, logo...'.format(rb, re))
    print('Eu venci, yeah!')
elif rb == 'papel' and re == 'tesoura':
    print('Eu joguei {} e você jogou {}, logo...'.format(rb, re))
    print('Você venceu, Grrr!')
elif rb == 'tesoura' and re == 'tesoura':
    print('Uai, eu joguei {} e você jogou {} também!'.format(rb, re))
    print('Empatamos, droga!')
elif rb == 'tesoura' and re == 'pedra':
    print('Eu joguei {} e você jogou {}, logo...'.format(rb, re))
    print('Você venceu, Grrr!')
elif rb == 'tesoura' and re == 'papel':
    print('Eu joguei {} e você jogou {}, logo...'.format(rb, re))
    print('Eu venci, yeah!')
else:
    print('Acho que cê fez algo de errado, tenta de novo aí!')
