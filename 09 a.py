n=input('Digite seu nome completo: ')
print(f'Número de caracter \033[0;32m{(len(n))}\033[m')
print(f'Caps On \033[1;34;40m{n.upper()}\033[m')
print(f'Caps Off \033[1;32;40m {n.lower()}\033[m')
s=n.strip()
sp=n.split()

print(f'Quantas letras tem o primeiro nome: \033[0;31m{len(sp[0])}\033[m')

