print('Vamos calcular sua média !')
n1=float(input('Digite a 1 nota: '))
n2=float(input('Digite a segunda: '))
media= (n1 + n2) // 2
if media == 5 or 5.1 or 5.2 or 5.3 or 5.4 or 5.5 or 5.6 or 5.7 or 5.8 or 5.9 or 6:
    print('Recuperação')
elif media < 5:
    print('Reprovado')
elif media > 7.0:
    print('Aprovado')
