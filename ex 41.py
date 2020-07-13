from time import sleep
print('Olá, está pronto para ser listado?!')
idade=int(input('Digite o ano em que nasceu: '))
t= (2020 - idade)
if t <=9:
     print('MIRIM')
elif t <=14:
     print('INFANTIL')
if t <= 19:
    print('JUNIOR')
elif t <= 20:
    print('MASTER')