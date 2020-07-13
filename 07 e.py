n = int(input('Digite um número para mostrar sua tabuada: '))

for c in range(1, 11):
    print('{0}x{1} = {2}'.format(n, c, (n * c)))