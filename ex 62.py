value1 = int(input('Digite o primeiro valor: '))
razao = int(input('Digite a razão: '))
c=1
mais=10
total=0
while mais != 0:
    total+=mais
    while c <= total:
        value1+=razao
        c+=1
        print(f'{value1}->', end='')
    mais=int(input('\nDeseja mais termos ? '))
print(f'{total} ← Número de termos')