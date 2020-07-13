import math
angulo=float(input('Digite o angulo: '))
s=math.sin(math.radians(angulo))
c=math.cos(math.radians(angulo))
t=math.tan(math.radians(angulo))
print('O seno do angulo \033[4;32m{}\033[m é \033[1;31m{}\033[m \n a tangente '
      '\033[1;31m{}\033[m\n e o coseno \033[1;31m{}\033[1;31m'.format(angulo,s,t,c))
