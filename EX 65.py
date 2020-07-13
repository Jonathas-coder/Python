parar = ''
contador = 0
vezes = 0
user = 0
while parar != 'S':
    contador+=1
    user+= int(input('Leitor de números inteiros: '))
    parar = str(input('Deseja parar?[S/N]: ')).upper()
    media = user / contador
print(f'{contador}← Quantidade de números. \n→ {user} a soma de todos os número  \nA média entre eles →{media}')