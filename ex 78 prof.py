lista=[]
high=0
low=0
for v in range(0,5):
    lista.append(int(input(f'Digite um número na posição {v}: ')))
    if v == 0:
        high=lista[v]
        low=lista[v]
    else:
        if lista[v] > high:
            high=lista[v]
        if lista[v] < low:
            low=lista[v]
print(f'A lista {lista}')
print(f'Maior  valor {high} na posição',end='')
for pos, valor in enumerate(lista):
    if  valor == high:
        print(f' {pos}..',end='')
print(f' Menor valor {low} na posição ', end='')
for pos, valor in enumerate(lista):
    if valor == low:
        print(f'{pos}..',end='')