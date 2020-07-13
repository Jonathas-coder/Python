number=[]
new=()
while True:
    new=int(input('Digite um número: '))
    if new not in number:
        number.append(new)
        print('Valor adicionado...')
    else:
        print('Valor não adicionado...')
    user=str(input('Deseja encerrar ? [S/N]')).upper()
    if 'S' in user:
        number.sort()
        print(f'Valores da lista {number}')
        break
