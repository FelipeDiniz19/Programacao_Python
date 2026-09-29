n1 = int(input("Digite seu numero:  "))

if n1 % 3 == 0 and n1 % 5 ==0:
    print("DIVISÍVEL POR 3 E 5")

elif n1 % 3 == 0:
    print("DIVISÍVEL APENAS POR 3")

elif n1 % 5 == 0:
    print("DIVISÍVEL APENAS POR 5")

else:
    print("POR NENHUM")