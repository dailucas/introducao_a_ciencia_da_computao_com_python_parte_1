
def conversor_de_segundos(entrada_segundos):
    dias = entrada_segundos//86400
    horas = (entrada_segundos - (dias * 86400))//3600
    minutos = (entrada_segundos - (dias*86400) - (horas*3600))//60
    segundos = (entrada_segundos - (dias*86400) - (horas*3600) - (minutos*60))
    print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.')
    return dias, horas, minutos, segundos


entrada_segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

conversor_de_segundos(entrada_segundos)


