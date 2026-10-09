print("-------- Tabuada ---------")

numero = input("Digite qual tabuada você quer: ")

while not numero.isdigit():
    print("Invalido, por favor digite um números inteiros")
    numero = (input("Digite qual tabuada você quer: "))


numero = int(numero)
contador = 1

while contador <= 10:
    print(f"{numero} X {contador} = {numero * contador}")
    contador += 1