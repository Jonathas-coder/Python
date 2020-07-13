year=int(input('Digite o ano que nasceu: '))
new= 2020 - year
limite= new - 18
menor= (year - 2020)*-1
t= 18 - menor
if new == 18:
    print('Está na hora de se alistar!')
elif new > 18:
    print(f'\033[1;31m{limite}\033[m anos atrasado !')
elif new < 18:
    print(f'Falta \033[1;30m{t}\033[m anos para se alistar!')
