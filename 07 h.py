
print('Iniciando programa...')
p=float(input('Digite o preço do produto: '))
t=(p*5/100)
sub=(p-t)
print('O desconto em liquidação é $\033[1;32m{}\033[m e o total é $\033[1;31m{}\033[m '.format(t,sub))