import random
computer=random.randint(0,9)
vezes=0
while True:
    print('-=-'*20)
    user=int(input('Digite um valor: '))
    soma= user+computer
    escolha=str(input('Você quer par ou impar [P/I]: ')).upper()
    if escolha == 'P' and soma %2 == 0:
        vezes += 1
        print('Você venceu !')
    if escolha == 'I' and soma %2 != 0:
        vezes += 1
        print('Você venceu')
    if escolha == 'P' and soma %2 !=0:
        print('~~'*25)
        print('***GAME OVER*** ')
        print(f'A soma entre {computer} e {user} é {soma} logo um número impar.')
        print(f'Você venceu {vezes} vezes !')
        break
    if escolha == 'I' and soma %2 ==0:
        print('~~'*25)
        print('***GAME OVER*** ')
        print(f'A soma entre {computer} e {user} é {soma} ou seja um número par.')
        print(f'Você venceu {vezes} vezes !')
        break