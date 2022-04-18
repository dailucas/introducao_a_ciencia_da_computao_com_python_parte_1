def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n -= 1
    if n == 0 and fat == 1:
        print('1')
    print(fat)

n = int(input('Digite o valor de n: '))
fatorial(n)