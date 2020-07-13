from math import trunc
print('=='*20)
print('           BANCO WOLF JOHN     ')
print('=='*20)
user=int(input('Qual valor você quer sacar: R$'))
while True:
    if user>= 50:
        total_50 = trunc(user/50)
        multiplicando_50 = total_50 * 50
        resto_50 = user - multiplicando_50          #Subtraindo os valores pra achar o resto
        #cédula 20
        if resto_50 <= 50:
            resultVinte = trunc(resto_50/20)
            multiplicando_20= resultVinte * 20
            resultado_Soma_vinte= multiplicando_20 + multiplicando_50
            subtrair = user - resultado_Soma_vinte
            # Cédula de 10
            if subtrair <=20:
                result_10=trunc(subtrair/10)
                result10= result_10 * 10
                if result10 <=10:
                    #cédula de 1
                    result_1=trunc(result10/1)
                    multiplicando_1= result_1*1
                    resultado_Soma_Termos= user - (multiplicando_50+multiplicando_20+multiplicando_1)
                    print('=='*20)
                    print(f'Total de {total_50} cédula de R$ 50'
                      f'\nTotal de {resultVinte} cédula de R$ 20'
                          f'\nTotal de {result_10} cédula de R$ 10'
                          f'\nTotal de {resultado_Soma_Termos} cédulas de R$ 1')
                    print("Volte sempre ao banco Wolf, tenha um bom dia!")
                    break