def primo(n):
    fator = 2
    contador = 1
    while fator <= 11:
        if n%fator == 0:
            contador += 1
            fator += 1
        else:
            fator += 1
    if contador >= 3:
        print('não primo')
    elif contador <= 2:
        print('primo')


n = int(input('Digite um número inteiro: '))
primo(n)