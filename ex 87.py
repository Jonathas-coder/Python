lista=[[0,0,0],[0,0,0],[0,0,0]]
soma=[]
for c in range(0,3):
    for l in range(0,3):
        lista[c][l]=int(input('Digite um número; '))
print('-='*30)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{lista[c][l]:^5}]',end='')
    print()
for l in range(0,3):
    for c in range(0,3):
        if lista[l][c]  % 2 == 0:
            soma.append(lista[c][l])
par=sum(soma)
c3=sum(lista[2])
maior=max(lista[1])
print(f'A soma dos números pares da lista é {par}')
print(f'A soma dos números na coluna 3 é {c3}')
print(f'O maior valor da segunda linha é {maior}')