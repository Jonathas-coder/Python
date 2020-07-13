from math import factorial
num=0
select=''
while select != 'S':
    num=int(input('Digite um valor: '))
    f = factorial(num)
    print(f'Fatorial de {num} é {f}')
    select=str(input('Deseja parar [N/S]: ')).upper()
