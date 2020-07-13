partidas=list()
jogadores=dict()
players=list()
while True:
    partidas.clear()
    jogadores["nome"]=str(input('Nome do jogador: ')).lower().capitalize()
    game=int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for c in range(0,game):
        partidas.append(int(input(f"Quantos gols na {c+1}º partida: ")))
    jogadores["gols"]=partidas[:]
    jogadores["total"]=sum(partidas[:])
    players.append(jogadores.copy())
    while True:
        opc=str(input('Deseja continuar [S/N]: ')).upper()
        if opc in 'SN':
            break
        else:
            print('Digite apenas S ou N')
    if opc == 'N':
        break
print('-'*40)
print('cod ',end='')
for i in jogadores.keys():
    print(f'{i!s:>7s}',end='')
print()
print('-'*40)
for k, v in enumerate(players):
    print(f'{k!s:<3} ', end='')
    for d in v.values():
        print(f'{d!s:<2s}   ', end='')            #A FUNÇÃO !s transforma a lista em string temporariamente.
    print()
print('-='*40)
while True:
    busca=int(input('Dados de qual jogador: '))
    if busca == 999:
        break
    if busca >= len(players):
        print(f'ERRO! o jogador {busca} não existe.')
    else:
        print(f'  LEVANTAMENTO DO JOGADOR {players[busca]["nome"]}')
        for i,v in enumerate(players[busca]["gols"]):
            print(f'{v} gols na {i+1}º partida ')
print('<<<VOLTE SEMPRE>>>')