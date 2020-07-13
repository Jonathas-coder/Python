r=float(input('Digite a distancia: '))
p1= (r)*1/2
p2= (r)*(45/100)
if r <= 200:
    print('O valor da passagem será R$\033[1;31m{}\033[m'.format(p1))
else:
    print('O valor da passagem R${}'.format(p2))
