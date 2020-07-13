def leiaint (msg):
    ok= False
    valor=0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            ok=True
            valor=int(n)
        else:
            print('ERRO. DIGITE UM NÚMERO INTEIRO!')
        if ok == True:
            break

n= leiaint(msg='Digite um número: ')


