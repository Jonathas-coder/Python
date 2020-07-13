
while True:
    print('-'*35)
    user=int(input('Quer ver a tabuada de qual valor: '))
    negativo=abs(user)*-1
    if user== negativo:
        print('Programa encerrado....')
        break
    print(f"""{user}x1={user}\n{user}x2={user*2}\n{user}x3={user*3}\n{user}x4={user*4}\n{user}x5={user*5}\n{user}x6={user*6}
{user}x7={user*7}\n{user}x8={user*8}\n{user}x9={user*9}""")
