par = 0
number = ()
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite só mais um: '))
number += n1, n2, n3, n4
time = number.count(9)
print(f'Você digitou os valores {number}')
print(f'Quantas vezes o número 9 apareceu {time}')
if n1 % 2 == 0:
    par += 1
if n2 % 2 == 0:
    par += 1
if n3 % 2 == 0:
    par += 1
if n4 % 2 == 0:
    par += 1
print(f'Vezes que números pares aparecem {par}')
print(f"""O valor 3 apareceu na posição {number.index(3)+1}º""")