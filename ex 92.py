nome=str(input("Nome: ")).lower().capitalize()
idade=int(input("Ano de nascimento: "))
ctps=int(input('Carteira de trabalho [0 se não possuir]: '))
date=list()
dados={'Nome':nome ,'Idade':2020-idade,'Ctps':ctps}
if ctps == 0:
    dados['Ctps']='Não possui'
if ctps !=0:
    dados['contrat'] = contrat = 2020 - int(input('Ano do primeiro contrato: '))
    dados['salario'] = salario = int(input('Salário: '))
    possivel = 35 - dados['contrat']
    if possivel <=0:
        dados["aposentar"]='Já é aposentado'
    else:
        dados["aposentar"]= possivel
    date.append(dados.copy())
    print('-='*30)
    print(f'Nome:{dados["Nome"]}'
          f'\nIdade: {dados["Idade"]} anos'
          f'\nAnos para se aposentar: {dados["aposentar"]}'
          f'\nSalario: {dados["salario"]}')
else:
    print('-='*30)
    for k, v in dados.items():
        print(f'{k}: {v}')

