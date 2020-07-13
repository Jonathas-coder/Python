num=int(input('Digite um número de 0 a 9999:'))
U= num // 1 % 10
D= num // 10 % 10
C= num // 100 % 10
M= num // 1000 % 10

print(f'Unidade \033[1;30m {U} \033[m')
print(f'Dezena \033[1;31m{D} \033[m')
print(f'Centena \033[1;32m{C}\033[m')
print(f'Milhar \033[7;30m{M}\033[m')

