altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

if altura < 1.40:
       print("Acesso negado por razões de segurança (altura mínima necessária: 1.40m)")
                
elif idade < 12 :
        print("Pagam R$ 15,00")

elif 12 <= idade <= 59 : 
        print("Pagam o valor cheio de R$ 30,00")

else:
    print ("Pagam metade do valor, R$ 15,00")



    

