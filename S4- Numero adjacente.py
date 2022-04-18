def numero_adjacente(numero):
    count = 0
    b = 0
    while numero > 0:
        a = numero % 10
        if a == b and count != 0:
            print('sim')
            return a, b
        else:
            b = a
            numero = numero //10
            count += 1
    print('não')


numero = int(input('Digite um número inteiro: '))
numero_adjacente(numero)
