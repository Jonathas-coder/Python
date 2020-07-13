barato=''
menor =contador=total=caro= 0
while True:
    print('-='*20)
    print('MERCADO JOHN S.A')
    print('-='*20)
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço do produto: R$'))
    total+=valor
    contador+=1
    if valor > 1000:
        caro+= 1
    if contador==1:
        barato=produto
        menor = valor
    else:
        if valor<menor:
            menor = valor
            barato=produto
    select=str(input('Deseja continuar [S/N]')).upper().strip()
    if select == 'N':
        print('~~'*20)
        print(f'Total a pagar: R${total:.2f}'
              f'\n{caro} produtos acima de R$1000\nProduto com menor preço foi {barato} custando R${menor:.2f} ')
        break
