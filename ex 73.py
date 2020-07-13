club=('Athletico','Atlético-MG','Atlético-GO','Bahia','Botafogo','Ceará','Corinthians','Coritiba','Flamengo','Fluminense'
      ,'Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Red Bull Bragantino','Santos','São Paulo','Sport',
      'Vasco da Gama')

print('G5 DO BRASILEIRÃO')
for c in range (0,4,1):
    print(f'{club[c]}')
print('\033[1;31mZona de rebaixamento\033[m')
for c1 in range (16,20,1):
    print(club[c1])
print(f'\033[1;32mClub em ordem alfabética\033[m:\n{sorted(club)}')
print(f"""O Bahia encontra-se na {club.index('Bahia')}º posição.""")















