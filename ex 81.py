lista=[]
while True:
    user=int(input('Digite um número: '))
    lista.append(user)
    op=str(input('Deseja encerrar?[S/N]: ')).upper()
    if op == 'S':
        print(f'Total de números digitados {len(lista)}')
        lista.sort()
        print(f'Números em decrescente {lista}')
        if 5 in lista:
            print('O número 5 está contido.')
            break