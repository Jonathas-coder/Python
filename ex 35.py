m1 =int(input('Digite a primeira medida: '))
m2 =int(input('Digite a segunda: '))
m3 =int(input('Digite a terceira: '))

if m1< m2+ m3 and m1> m2-m3 \
        and m2< m3+m1 and m2> m3-m1\
        and m3< m1+m2 and m3> m2-m1:
    print('\033[1;30mÉ possivel fazer um triangulo\033[m !')
else:
    print('\033[1;30mNão é possivel fazer um triangulo\033[m!')