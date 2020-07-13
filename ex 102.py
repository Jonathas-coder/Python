def fatorial (n,show=0):
    f=1
    for c in range(n,0,-1):
        if show == True:
            print(f'{c}',end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f*=c
    return f
user=5
print(fatorial(user,True))







"""def fatorial(n,show=0):
    n = user
    t = 0
    if show == True:
        print(f'{user}',end='')
        for c in range(n,0,-1):
            t+=1
            n*=t
            print(f'{t} ', end='')
            if c > 1:
                print('x ',end='')
        print(f'= {n}')
    else:
        for c in range(n,1,-1):
            t+=1
            n*=t
        print(f'Fatorial de {user} é: {n}')"""