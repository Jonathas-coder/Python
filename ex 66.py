user=0
somar=0
somar_user=0
while True:
    somar+=1
    user=int(input('Digite números inteiros (\033[1;34m999 stop the program\033[m):'))
    if user == 999:
            break
    somar_user+=user
print(f'A soma dos {somar} valores é {somar_user}')