from time import sleep
b=int(input('Digite o ano, direi se é bissexto: '))
print('\033[1;35mProcessando...\033[m')
sleep(1)
if b % 4 == 0:
    print(f'{b} é um ano bissexto !')
else:
    print(f'{b} não é bissexto !')
