import random
n=str(input('Digite o primeiro nome: '))
n2=(input('Digite o segundo: '))
n3=(input('Digite o terceiro: '))
n4=(input('Digite o quarto: '))
f=(n,n2,n3,n4)
g=random.choice(f)
print('O pokemon lendário vai para {:=^20}'.format(g))
print('Parabéns \033[7m{}\33[m ! seu pokemon será entregue amanhã'.format(g))
