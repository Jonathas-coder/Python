altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))**2
imc=peso//altura
if imc < 18.5:
    print('\033[1;34mAbaixo do peso !\033[m')
elif imc >= 18.5 and imc <=25:
    print('\033[1;31mPeso ideal\033[m !')
elif imc >= 25 and imc <=30:
    print('\033[1;30mSOBREPESO\033[m')
elif imc >= 30 and imc <=40:
    print('\033[1;35mObesidade\033[m')
elif imc >40:
    print('\033[1;33;41mvocê vai morrer filho da puta kkk !\033[m')
print(f'Seu imc é {imc}')
