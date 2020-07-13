mulher=0
nomevelho=''
homemvelho=0
somaidade=0
for pessoa in range(1,5):
    print(f'---------{pessoa}° pessoa---------')
    nome=str(input(('Nome:')))
    idade=int(input('Idade: '))
    somaidade=idade
    sexo=str(input('Sexo M/F: ')).strip()
    if pessoa == 1 and sexo in 'Mm':
        homemvelho=idade
        nomevelho=nome
    elif sexo in 'Mm' and idade > homemvelho:
        homemvelho=idade
        nomevelho=nome
    if sexo in 'Ff' and idade <20:
        mulher+=1

media=somaidade/4
print(f'A idade do homem mais velho é {homemvelho} e o nome é {nomevelho} !')
print(f'A média de idade entre esse grupo é {media}')
print(f'O número de mulheres menores que 20 é {mulher}')
