print("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA""")
select=0
while select != 5:
    select = int(input('Qual sua opção: '))
    if select==5:
        print('Fim do programa.')
        exit()
    if select >=6:
        print('Opção inválida''')
        exit()
    value1=int(input('Qual o 1º valor: '))
    value2=int(input('Qual o 2 º valor: '))
    if select == 1:
        print(f'A soma entre {value1} e {value2} é {value1+value2}')
    elif select == 2:
        print(f'A multiplicação entre os valores é {value1*value2}')
    elif select == 3:
        if value1>value2:
            print(f'Entre os valores o maior é {value1}')
        if value2>value1:
            print(f'Entre os valores o maior é {value2}')
    if select == 4:
        value1 = int(input('Qual o 1º valor: '))
        value2 = int(input('Qual o 2 º valor: '))
    if select == 5:
        exit()
