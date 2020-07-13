import random
from time import sleep
lista=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
c=c1=0
print('-='*30)
print(f"""{' '*20}{'JOGO DA MEGA SENA'}""")
print('-='*30)
user=int(input('Digite quantos jogos você deseja: '))
print(f"""{'=-'*10}SORTEANDO {user} JOGOS{'=-'*10}""")
while c <= 5:
    for n in range(0,user):
        for m in range(0,6):
            lista[n][m]=(random.randint(0,60))
    c+=1
user-=1
lista.sort()
while c1 <=user:
    sleep(1)
    print(f'\033[1;35mJogo {c1+1}\033[m: {lista[c1]}')
    c1+=1
print(f"""{'=-'*10}BOA SORTE!{'=-'*10}""")
