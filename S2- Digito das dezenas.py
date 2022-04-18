def dezenas(numero):
    contador = 0
    dezena = 0
    while contador < 2:
        dezena = numero%10
        numero = numero//10
        contador += 1

    print(f'O dígito das dezenas é {dezena}')
    return dezena


numero_inteiro = int(input('Digite um número inteiro: '))

dezenas(numero_inteiro)