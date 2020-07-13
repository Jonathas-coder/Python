from time import sleep


def contador (i,f,p ):
    print('='*30)
    print('Contagem de 0 a 10:')
    if p < 0:
        p*=-1
    if p == 0:
        p=1
    for n in range(1,11):
        sleep(0.3)
        print(f'{n} ',end='',flush=True)
    print()
    print('='*30)
    print('Contagem de 10 até 0 de 2 em 2:')
    for nu in range(10, -1, -2):
        sleep(0.3)
        print(f'{nu} ', end='',flush=True)
    print()
    print('='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('='*30)
    if i > f:
        for c2 in range(i,f+1, p):
            sleep(0.3)
            print(f'{c2} ',end='',flush=True)

    if i < f and p == 1:
        for c2 in range(i, f+1, p):
            sleep(0.3)
            print(f'{c2} ', end='',flush=True)
        print()
        print('=' * 30)

    if i > f:
        for c2 in range(i+1, f,-p):
            sleep(0.5)
            print(f'{c2-1} ', end='',flush=True)
        print()
        print('=' * 30)


i2=int(input('Digite o inicio: '))
f2=int(input('Digite o final: '))
p2=int(input('Digite o passo: '))
contador(i=i2, f=f2, p=p2)
