def voto(n):
    from datetime import date
    ano= date.today().year
    idade= ano - n
    if idade <= 18:
        return f'{idade} anos, não vota.'
    elif idade >= 18 and idade <= 65:
        return f'{idade} anos, voto obrigatorio.'
    if idade >= 65:
        return f'{idade} anos, volto opcional.'


print('='*20)
user=int(input('Que ano você nasceu: '))
print(voto(n=user))