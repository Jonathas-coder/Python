from time import sleep
def maior (*num):
    print('='*20)
    print(f'Analisando números... ')
    for l,v in enumerate(num):
        for d in v:
            sleep(0.3)
            print(f'{d}-> ', end='',flush=True)
    print()
    maior2=0
    for k,n in enumerate(num):
        maior2=max(n)
    sleep(0.3)
    print(f'O maior número foi {maior2}')


f = [0, 4, 5, 6, 8, 4]
maior(f)
f = [0, 4]
maior(f)
f = [12, 6, 8, 4]
maior(f)