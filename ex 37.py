print(""" Conversor de números.
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL""")
opç =int(input('Sua opção: '))
num=int(input('O número que será convertido:'))
if opç == 1:
    print(f'O numero {num} em binario é {bin(num)[2:]}')
elif opç == 2:
    print(f'O numero {num} em octal é {oct(num)[2:]}')
elif opç == 3:
    print(f'O numero {num} em hexa é {hex(num)[2:]}')
else:
    print('Opção invalida !')
