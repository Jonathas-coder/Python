muie=list()
age=list()
people=list()
femea = {}
p=0
while True:
    p+=1
    nome=str(input("Nome: ")).lower().capitalize()
    idade=int(input('Qual a idade: '))
    sexo=str(input('Sexo [F/M]')).upper()
    opc=str(input('Deseja continuar [S/N]: ')).upper()
    age.append(idade)
    media = sum(age) / 2
    pessoas = {'nome': nome, 'idade': idade, 'sexo': sexo}
    people.append(pessoas.copy())
#while como condição de parada.
    while opc != 'S' and opc != 'N':
        opc = str(input('Deseja continuar [S/N]: ')).upper()
    if opc == 'N':
        break
print('-=' * 30)
print(f'Quantas pessoas foram cadastradas: \033[1;31m{p}\033[m'
      f'\nMédia de idade: \033[1;31m{media}\033[m')

#usando enumerate na lista people para achar as pessoas com 'f' no dicionario
for key,va in enumerate(people):
    if va["sexo"] == 'F':
        muie.append(va["nome"])      #usando uma lista para armazenar todos os nomes no dicionario que tiverem 'F'

print('Garotas na lista:',end='')
for c in range (0,len(muie)):       #O for esta lendo cada objeto na lista baseado com o numero(len) de pessoas na lista 'muie'
    print(f' {muie[c]}.',end='')

#usando o for para ler quantos valores (v) na lista people são maiores que a meida.
for k,v in enumerate(people):
    if v['idade'] >= media:
        print(f'\nIdade acima da média: {(v["nome"])} com \033[1;31m{v["idade"]}\033[m anos.')
