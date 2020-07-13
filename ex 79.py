valores=[]
new=[]
new2=[0]
while True:
    new=int(input('Digite um número: '))
    for v in valores:
        if new in valores:
            new2=new
    if new in valores:
        print("Valor não adicionado")
    user = input(str(('Deseja encerrar[S/N]: '))).upper()
    if new in valores :
        valores.remove(new)
    if valores != new2:
        valores.append(new)
        if user == 'S':
            print('=-'*20)
            print(f'Valores em ordem:{sorted(valores)}')
            print('=-'*20)
            break
        #continue

