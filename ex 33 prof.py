
print('---' * 23)
print(('VOU SOLICITAR 3 NÚMEROS ABAIXO E DIZER QUAL O MAIOR E O MENOR!!!', 'red'))
print('---' * 23)
num1 = int(input('DIGITE UM NÚMERO: '))
num2 = int(input('DIGITE OUTRO NÚMERO: '))
num3 = int(input('AGORA O ÚLTIMO NÚMERO: '))
#Verificando quem é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#Verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f'O MAIOR NÚMERO DIGITADO FOI \033[1;34m{maior}\033[m.')
print(f'O MENOR NÚMERO DIGITADO FOI \033[1;35m{menor}\033[m.')


