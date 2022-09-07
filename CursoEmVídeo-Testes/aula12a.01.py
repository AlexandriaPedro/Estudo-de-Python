nome = str(input('Qual seu nome? '))
if nome == 'Pedro':
    print('Que nome bonito, hein!')
elif nome == 'Arthur' or nome == 'Salomão' or nome == 'Enoque':
    print('No véi, que nome pica, mané!')
elif nome in 'Gustavo Jõao Leonardo':
    print('Seu nome é doidera, jow!')
else:
    print('Seu nome é show até!')
print('Tenha um bom dia, {}!'.format(nome))
