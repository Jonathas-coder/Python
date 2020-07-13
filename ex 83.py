user=str(input('Digite uma expressão: ')).strip()
lista=[]
for si in user:
    if si == '(':
        lista.append('(')
    elif si == ')':
        if len(lista) > 0:
            lista.pop()  #ele vai apagar '(' sempre que digitar ')' , caso não tiver '(' e digitar ')' ele nao vai apagar.
        else:
            lista.append(')')
            break
if len(lista) ==0:
    print('Expressão válida')
else:
    print('Expressão inválida')