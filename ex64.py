contador=0
user=0
num=0
while user != 999:
    print('~*'*20)
    num+=int(input('\033[1;32mLeitor de número inteiro:\033[m '))
    print('~*' * 20)
    contador+=1
    user=int(input('Se deseja parar digite \033[1;34m[999]\033[m: '))
print(f'A soma entre eles é → {num}')
print(f'Quantos números foram digitados → {contador}')
