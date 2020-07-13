from random import randint
comp= randint (0,7)
print('\033[1;34m-=-\033[m' * 20)
print('Estou pensando...')
print('\033[1;35m-=-\033[m' * 20)
print('Tente adivinhar o número que pensei')
jog=0
soma=0
nome=str(input('\033[7mQual seu nome ?\033[m\n'))
while jog != comp:
    jog=int(input('\033[1;34m*§*§*§*\033[mQual o número?\033[1;35m*§*§*§*\033[m\n '))
    print('\033[1;34mPROCESSANDO...\033[m')
    if jog == comp:
        print('Parabéns você me venceu !')
    if jog != comp:
        soma+=1
if soma <= 2:
    print(f'Você precisou apenas de {soma} tentativas ! \033[7mvocê é foda {nome}\033[m')
else:
    print(f'Que noob, precisou de {soma} tentativas !! ')



