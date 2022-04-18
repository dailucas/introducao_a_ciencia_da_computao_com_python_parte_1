def par_impar(numero):
    if numero%2 == 0:
        print('par')
    else:
        print('ímpar')

numero = int(input('Digite um numero para verificar se é par ou ímpar: '))

par_impar(numero)