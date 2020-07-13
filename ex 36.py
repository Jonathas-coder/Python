import math
casa = float(input('Valor da casa:'))
salario = float(input('Seu salário:'))
anos = float(input('Quantos anos: '))*12
r= casa // anos
porcem = (salario * 30) // 100
tr= (r*anos)
t1=tr//1000
if r < porcem:
    print('Voce pode pagar em \033[1;31m{}\033[m meses !'.format(math.trunc(t1)))
else:
    print('Emprestimo negado')
