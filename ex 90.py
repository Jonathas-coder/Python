name=str(input('Nome: '))
media=float(input(f'Média de {name}: '))
alunos={'Nome':name,'media':media}
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')
