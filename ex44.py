produto=float(input('Digite o valor do produto: '))
print("""[1] Pagamento a vista 10% de desconto
[2] Pagamento a vista no cartão 5% 
[3] Até 2x no cartão
[4] 3x ou mais no cartão 20%""")
o=int(input('Digite o que prefere:'))
#calculando
valor=(produto * 10) // 100
v1=produto-valor
cartao=(produto * 5) // 100
c1=produto-cartao
duas=produto//2
tres=(produto * 20) // 100
tres1=(produto // 3) + tres
if o == 1:
    print(f'Desconto de \033[1;30m{valor}\033[m total R$ \033[1;31m{v1}\033[m')
elif o == 2:
    print(f'Pagamento a vista no cartão terá desconto de \033[7m{cartao}\033[m valor final R$\033[1;31m{c1}\033[m')
elif o == 3:
    print(f'Parcelando de 2x \033[1;30m{duas}\033[m')
elif o == 4:
    print(f'Parcelando 3x, juros de \033[1;30m{tres}\033[m valor final de cada parcela: \033[1;35m{tres1}\033[m')
else:
    print('Invalido')
