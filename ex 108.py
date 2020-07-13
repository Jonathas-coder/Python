from ex107 import moedas

user=int(input('Digite um número: '))
print(f'Aumento de 10% do número {user} = {moedas.aumentar(user)}')
print(f'Diminuindo 13% = {moedas.moedaDiminuindo(user)}')
print(f'Metado do número = {moedas.metade(user)}')
print(f'O dobro = {moedas.dobro(user)}')