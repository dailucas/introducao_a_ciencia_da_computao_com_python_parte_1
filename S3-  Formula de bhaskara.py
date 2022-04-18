import math

def bhaskara(a,b,c):
    x1 = 0
    x2 = 0
    delta = ((b)**2) - 4 * a * c
    if delta > 0:
        x1 = (-(b) + math.sqrt(delta))/(2 * a)
        x2 = (-(b) - math.sqrt(delta))/(2 * a)
        if x1 > x2:
            print(f'as raízes da equação são {x2} e {x1}')
        else:
            print(f'as raízes da equação são {x1} e {x2}')

    elif delta == 0:
        x1 = (-(b))/(2 * a)
        print(f'a raiz desta equação é {x1}')
    elif delta < 0:
        print('esta equação não possui raízes reais')

a = int(input('digite o valor de ax**2:'))
b = int(input('digite o valor de bx: '))
c = int(input('digite o valor de c: '))

bhaskara(a,b,c)


