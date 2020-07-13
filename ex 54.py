from datetime import date
ano= date.today().year
totmaior=0
totmenor=0
for c in range (1,8):
    user=int(input(f'Digite o ano em que nasceu {c}º: '))
    if ano - user <= 21:
        totmenor+=1
    else:
        totmaior+=1
print(f'Número de maiores de idade {totmaior}')
print(f'Número de menores {totmenor}')
