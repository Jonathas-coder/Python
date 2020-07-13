print('GERADOR DE PA')
print('-='*10)
first=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razão da PA: '))
c=1
while c <=10:
    print(f'{first}->',end='')
    first+=razao
    c+=1
print('FIM')
