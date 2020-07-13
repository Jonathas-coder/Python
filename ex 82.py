lista=[]
impar=[]
par=[]
while True:
    user=int(input('Digite um número: '))
    lista.append(user)
    if user % 2== 0:
        par.append(user)
    else:
        impar.append(user)
    op=str(input('Deseja continuar[S/N]: ')).upper()
    if op == 'S':
        lista.sort()
        print('=-'*30)
        print(f'\Lista com total de números {lista}')
        print(f'Lista com números impares {impar}')
        print(f'Lista com números pares {par}')