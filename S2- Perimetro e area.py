def quadrado(l):
    perimetro =  l * 4
    area = l ** 2
    print(f'perímetro: {perimetro} - área: {area}')
    return perimetro, area

l = int(input('Digite o valor correspondente ao lado de um quadrado: '))

quadrado(l)