print('Olá, vamos analisar números!')
n=int(input('Digite um numero:'))
d=int(n)*2
t=int(n)*3
r=int(n)**2

print('O dobro do número \033[1;36m{}\033[m é \033[1;31m{}\033[m o triplo \033[1;33m{}\033[m a potencia {}'.format(n,d,t,r))
