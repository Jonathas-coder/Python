lista=list()
while True:
    nome=str(input('Nome: ')).upper().strip()
    nota1=float(input('Nota: '))
    nota2=float(input('Nota: '))
    media=nota1+nota2 / 2
    lista.append([nome,[nota1,nota2],[media]])
    op = str(input("Quer continuar [S/N]: ")).strip().upper()
    if 'N' in op:
        break
print('-=-'*20)
print(f'{"""No.""":<4}{"""NOME""":<10}{"""MÉDIA""":>8}')
for i, a in enumerate(lista):
    print(f'{i}    {a[0]}       {a[2]}')
while True:
    opc=int(input("Qual aluno deseja ver?[999 para interromper]: "))
    if opc == 999:
        break
    if opc <= len(lista) -1 :
        print(f'Aluno: {lista[opc][0]}--{lista[opc][1]}')