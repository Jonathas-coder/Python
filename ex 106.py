def helpi (txt=False):
    user=list()
    user.append(txt)
    while True:
        user.clear()
        user.append( str(input('-> FUNÇÃO OU BIBLIOTECA: ')).strip().lower())
        if user[0] == 'fim':
            break

        elif user != 'fim':
            help(user[0])
            user.clear()

helpi()