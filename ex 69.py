women20=0
homem=0
maior=0
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade=int(input('Qual a idade: '))
    if idade > 18:
        maior+=1
    sexo=str(input('Qual o sexo [M/F]: ')).upper()
    if sexo == 'M':
        homem+=1
    else:
        print('DIGITE UM SEXO VÁLIDO POR FAVOR.')
        sexo = str(input('Qual o sexo [M/F]: ')).upper()
    if idade <20 and sexo == 'F':
        women20+=1
    print('-'*15)
    continuar=str(input('Deseja continuar [S/N]: ')).upper()
    if continuar == 'N':
        print(f'Total de pessoas maiores de 18 anos:{maior}\nAo todo temos {homem} homens cadastrados'
              f'\nTotal de mulheres com menos de 20 anos: {women20}')
        break