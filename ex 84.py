people=[]
dado=[]
np=0
while True:
    np+=1
    name=str(input('Digite o nome: '))
    peso=int(input('Digite o peso: '))
    dado.append(name)
    dado.append(peso)
    people.append(dado[:])
    dado.clear()
    op=str(input('Deseja parar [S/N]: ')).upper()
    if op == 'S':
        p=max(people)
        l=min(people)
        print(f'A pessoa mais pesada foi {p[0]}')
        print(f'A pessoa mais leve foi {l[0]}')
        print(f'Número de pessoas listadas {np}')
        break