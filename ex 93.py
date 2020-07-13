name=str(input('Qual é o nome do jogador: ')).lower().capitalize()
p=int(input(f'Quantas partidas o {name} jogou? '))
gols=list()
total=list()
club = {'Nome': name, 'gols': gols,'total':total}
for c in range(0,p):
    gol=int(input(f'Quantos gols na {c+1}º partida: '))
    gols.append(gol)
total1=sum(gols)
total.append(total1)
print('-='*30)
print(f'O jogador {name} jogou {p} partidas')
for p, g in enumerate(gols):
    print(f'=> Na {p+1}º partida fez {g} gols')
print(f'Total de {total[0]} gols.')