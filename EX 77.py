palavras='amar','matar','destruir','cancelar','vingança','obliterar','arduin','transformar'
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra,end='')



    """if c % 1 == 0:
        print(palavra[c])
    if 'u'in palavra[c]:
        print(f'Vogal a repete {palavra[c].count("u")}x')"""


