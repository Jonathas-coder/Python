lista=[[],[]]
for c in range(0,7):
    user=int(input('Digite um número: '))
    if user % 2 != 0:
        lista[0].append(user)
    else:
        lista[1].append(user)
lista.sort()
print(f'Números impares {lista[0]}\nNúmeros pares {lista[1]}')