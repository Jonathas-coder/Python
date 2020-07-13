n=int(input('Qual o fatorial: '))
fator=n
for c in range (n-1,0,-1):
    fator*=c
print(f'Fatorial de {n} é {fator}')
