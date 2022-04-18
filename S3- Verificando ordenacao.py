def ver_ordenacao(a,b,c):
    if a < b and b < c:
        print('crescente')
    else:
        print('não está em ordem crescente')

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero '))
ver_ordenacao(a,b,c)