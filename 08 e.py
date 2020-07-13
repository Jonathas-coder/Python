import random
n1=(input('Digite o primeiro nome: '))
n2=(input('Digite o segundo: '))
n3=(input('Digite o terceiro: '))
n4=(input('Digite o quarto: '))
f=[n1,n2,n3,n4]
seq=random.sample(f,4)
print('A primeira apresentação é:\033[1;31m ',seq)
