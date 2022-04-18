def soma_dos_digitos(n):
    soma = 0
    ultimo_digito = 0
    while n > 0:
        ultimo_digito = n % 10
        soma = soma + ultimo_digito
        n = n//10
    print(soma)

n = int(input('Digite um número inteiro: '))

soma_dos_digitos(n)