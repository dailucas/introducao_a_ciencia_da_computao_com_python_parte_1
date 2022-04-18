def numeros_impares(n):
    contador = 0
    impares = 1
    while contador < n:
        print(f'{impares}', end='\n')
        contador += 1
        impares += 2
    return impares

n = int(input('Digite o valor de n: '))

numeros_impares(n)