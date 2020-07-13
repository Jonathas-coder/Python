m1=int(input('Digite a primeira medida: '))
m2=int(input('Digite a segunda medida: '))
m3=int(input('Digite a terceira medida:' ))
if m1 < m2 + m3 and m2< + m1+m3 and m3 < m1+m2:
    print('Pode formar um triangulo',end=' ')
    if m1 == m2 and m2 == m3:
        print('EQUILATERO')
    elif m1 != m2 != m3 !=m1:
        print('ESCALENO')
    else:
        print('ISÓCELES')


