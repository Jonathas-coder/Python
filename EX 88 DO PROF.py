import random
lista=[]
dados=[]
tot=1
quant=int(input("Quantos jogos você quer? "))
while tot <= quant: #ENQUANTO TOT NÃO CHEGAR EM QUANT ELE VAI CONTINUAR RODANDO.
    c=0
    while True:
        num=random.randint(1,60)
        if num not in lista:      #se não estiver na lista = faça algo
            lista.append(num)       #VAI ADICIONAR O VALOR SEM REPETIR
            c+=1
        if c >=6:
            break
    lista.sort()            #VAI ORGANIZAR TUDO
    dados.append(lista[:])  #TODA VEZ QUE LISTA PEGAR 6 NUMEROS DADOS VAI COPIAR PRA DENTRO DELA
    lista.clear()           #VAI APAGAR TODA VEZ QUE PEGAR, PRA NÃO REPETIR OS NUMEROS DENTRO DE DADOS
    tot+=1
for l,d in enumerate(dados): #l É A POSIÇÃO E d É O VALOR
    print(f'Jogo {l+1}: {d}')