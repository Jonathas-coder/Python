extenso=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
         'treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    user = int(input('Digite um número entre 0 e 20: '))
    if user <=20:
        for c  in range (0,user,30):
         print(f'O número {user} por extensso é {extenso[user]}')
        break
    elif user >20 or user <0:
        print('Tente novamente...')
        user = int(input('Digite um número entre 0 e 20: '))
        if user <= 20:
            for c in range(0, user, 30):
                print(f'O número {user} por extensso é {extenso[user]}')
            break