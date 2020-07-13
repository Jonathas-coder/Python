def ficha(jog='<desconhecido>',gol=0):
    print(f'O jogador {jog} fez {gol} gol(s)')

n=str(input('Digite o nome do jogador: '))
g=input('Digite quantos gols foram marcados: ')
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)











"""def ficha(nome=str,gols=0):
    if nome == None:
         return '<desconhecido>'
    if gols == None:
        return '0 gols'
    print(nome)
    return(f'O jogador {nome} fez {gols} gols !')
print('='*20)
user=str(input('Digite o nome do jogador: '))
use=(input('Quantos gols foi marcado: '))
print(ficha(nome=user,gols=False))"""