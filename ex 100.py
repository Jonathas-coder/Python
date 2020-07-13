from random import randint
def sorteio (one):
    one.append([randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20)])
    print(f'Números gerados ! {one}')
def soma (one):
    s1=0
    s=list()
    for k, v in enumerate(one):
        for d in v:
            if d % 2 == 0:
                s.append([d])
        for k, v in enumerate(s):
            for d in v:
                s1+=d
    print(f'A soma dos pares da lista foram: {s1} ', end='')



j=list()
sorteio(j)
soma(j)