import random
print('='*60)
print("""Tente me vencer, escolha: Pedra Papel ou Tesoura!
[1] Tesoura
[2] Papel
[3] Pedra""")
print('='*60)
user=str(input('Escolha: '))
n1 = str('Papel')
n2 = str('Tesoura')
n3 = str('Pedra')
pc=random.choice([n1,n2,n3])
if user == 'tesoura' and pc == n3:
    print(f'Você perdeu, escolhi {pc} e você tesoura. HAHAHA!')
elif user == 'tesoura' and pc == n1:
    print(f'Droga, eu perdi! você escolheu tesoura e eu escolhi {pc}')
elif user == 'tesoura' and pc == n2:
    print('HMMM... Temos um empate!')
elif user == 'papel' and pc == n2:
    print(f'Voce perdeu, escolhi \033[1;31m{pc}\033[m e você \033[1;35mpapel\033[m!')
elif user =='papel' and pc == n3:
    print(f'Droga! você ganhou! escolhi \033[1;31m{pc}\033[m!')
elif user == 'papel' and pc == n1:
    print('Temos um empate!')
elif user == 'pedra' and pc == n1:
    print(f'Você perdeu! escolhi {pc} e você pedra !')
elif user == 'pedra' and pc == n2:
    print(f'Porra! você venceu, escolhi {pc} e você pedra.')
elif user == 'pedra' and pc ==n3:
    print('Opa! parece que temos um empate!')
else:
    print('invalido')

