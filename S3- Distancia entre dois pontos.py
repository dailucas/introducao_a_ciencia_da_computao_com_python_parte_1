import math

def distancia(x1,y1,x2,y2):
    d = math.sqrt((((x1-x2)**2)) + ((y1 - y2)**2))
    if d > 10:
        print('longe')
    else:
        print('perto')


x1 =int(input('digite a coordenada x1: '))
y1 =int(input('digite a coordenada y1: '))
x2 =int(input('digite a coordenada x2: '))
y2 =int(input('digite a coordenada y2: '))

distancia(x1,y1,x2,y2)