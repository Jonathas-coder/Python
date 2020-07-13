import random
from operator import itemgetter
jogador={'Jogador1': random.randint(1,6),
         'Jogador2': random.randint(1,6),
         'Jogador3': random.randint(1,6),
         'Jogador4': random.randint(1,6),
         }
ranking=list()
for k, v in jogador.items():
    print(f'{k} tirou o valor: {v}')
ranking=sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}º {v[0]} com {v[1]}')
print(ranking)