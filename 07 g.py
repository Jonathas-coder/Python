print('Olá, vamos calcular um pouco...')
a=int(input('Digite altura da parede: '))
l1=int(input('Digite a largura: '))
m=(a*l1)/2
print('A quantidade de tinta nescessária \033[7;30m{}\033[m'.format(m))
