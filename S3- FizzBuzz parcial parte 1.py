def fizzbuzz(numero):
    if numero % 3 == 0:
        print('Fizz')
        return numero
    else:
        print(numero)
        return numero


numero = int(input('Digite um numero: '))


fizzbuzz(numero)