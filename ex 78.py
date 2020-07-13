valores= []
for v in range(0,5):
    valores.append(int(input('Digite um valor: ')))
maior=max(valores)
menor=min(valores)
print('=-'*20)
print(f'Você digitou os valores: {valores}')
print(f'Maior valor {maior}  na posição {valores.index(maior)}'
      f'\nMenor valor {menor} na posição {valores.index(menor)}')