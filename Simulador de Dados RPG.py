import random
r = 'S'
print('='*30)
print('Simulador de Dados - RPG')
print('='*30)
while r == 'S':
    dado = int(input('''Estes são os disponíveis no momento:
[ 1 ] D4
[ 2 ] D6
[ 3 ] D8
[ 4 ] D10
[ 5 ] D12
[ 6 ] D20
[ 7 ] D100
Digite seu dado: '''))
    if dado == 1:
        resultado = random.randint(1, 4)
        print('O resultado é {}.'.format(resultado))
    elif dado == 2:
        resultado = random.randint(1, 6)
        print('O resultado é {}.'.format(resultado))
    elif dado == 3:
        resultado = random.randint(1, 8)
        print('O resultado é {}.'.format(resultado))
    elif dado == 4:
        resultado = random.randint(1, 10)
        print('O resultado é {}.'.format(resultado))
    elif dado == 5:
        resultado = random.randint(1, 12)
        print('O resultado é {}.'.format(resultado))
    elif dado == 6:
        resultado = random.randint(1, 20)
        print('O resultado é {}.'.format(resultado))
    elif dado == 7:
        resultado = random.randint(1, 100)
        print('O resultado é {}.'.format(resultado))
    else:
        print('Essa opção não existe')
    r = str(input('Deseja rolar outro dado? [S/N] ')).upper()
print('Fim')
