n=str(input('Digite a frase:')).strip().upper()
dividir=n.split()
junto=''.join(dividir)
inverso=''
print(junto)
for letra in range (len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Sim, é Palíndromo')
else:
    print('Não')
