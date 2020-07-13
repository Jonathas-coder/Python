n=input('Digite uma frase:')
f=n.strip().lower()
c =n.count('a')
f1=f.find('a')
f2=f.rfind('a')

print(f'A letra a aparece \033[1;31m{c}\033[m vezes')
print('Quando aparece \033[1;30m{}\033[m outra \033[1;30m{}\033[m'.format(f1,f2))