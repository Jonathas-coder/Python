lista=[]
for c in range(0,5):
    n=int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Número adicinado ao final da lista...')
    else:
        pos=0
        while pos < len(lista):
            if n  < lista[pos]:
                lista.insert(pos,n)
                print(f'Número {n} adicionado na posição {pos}')
                break
            pos+=1
print('*='*30)
print(f'Os valores digitados em ordem são {lista}')




























"""lista=[]
c=0
num=0
while c != 4:
    c+=1
    num=int(input('Digite um número: '))
    if lista == []:
        lista.append(num)
        print('Adicionado a lista...')
    elif num < max(lista):
        lista.append(num)
        print('Adicionado no final...')
    elif num > min(lista):
        lista.insert(0,num)
    else:
        for p, n in enumerate(lista):
            if n > num:
                lista.insert(p,n)
                print(f'{num} na posição {p}')
            if n == num:
                break"""



