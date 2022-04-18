def fizzbuzz(numero):
    if numero % 5 == 0:
        print('Buzz')
        return numero
    else:
        print(numero)
        return numero


numero = int(input('Digite um numero: '))


fizzbuzz(numero)