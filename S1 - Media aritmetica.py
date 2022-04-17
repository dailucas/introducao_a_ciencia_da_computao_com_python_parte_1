def media_aritmetica(a,b,c,d):
    media = (a + b + c + d)/4
    print(f'A média aritmética é {media}')
    return media

a = int(input('Digite a primeira nota: '))
b = int(input('Digite a segunda nota: '))
c = int(input('Digite a terceira nota: '))
d = int(input('Digite a quarta nota: '))

media_aritmetica(a,b,c,d)