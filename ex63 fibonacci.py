termo1 = 0
termo2 = 1
contador = 2
user = int(input('Digite quantos termos de Febenucci deseja ver: '))
while contador <= user:
    termo3 = termo1+termo2
    print(f'{termo3} →', end='')
    contador += 1
    termo1 = termo2
    termo2 = termo3
print('FIM')
