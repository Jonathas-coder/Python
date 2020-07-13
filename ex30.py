from time import sleep
n1=int(input('Digite o número: '))
if n1 % 2 == 0:
    print('\033[0;30mProcessando...\033[m')
    sleep(1)
    print('Numero par')
else:
    print('Numero impar')