n1=float(input('Digite seu salário: '))
p1=(n1*10)/100
p2=(n1*15)/100

if n1 > 1250:
    print(f'O aumento será de R$ \033[7m{p1}\033[m !')
if n1< 1250:
    print(f'O aumento será de R$ \033[1;33m{p2}\033[m !')

