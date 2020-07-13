n1=int(input('Digite a sua velocidade na rodovia:'))
if n1 > 80:
    multa= (n1 - 80) *7
    print('Multa de R$\033[1;31m{}\033[m'.format(multa))
else:
    print('Está tudo bem!')