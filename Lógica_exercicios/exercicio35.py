idade = int(input("Digite a sua idade: "))
print("")
estudante = input("Você é estudante? (S/N): ").upper()
print("")

ingresso = 30
meia = ingresso - (ingresso * 0.50)

if estudante != 'S' and estudante != 'N':
    print("Por favor, digite apenas Sim ou Não (S/N).")

elif idade > 12 and idade < 60 and estudante == 'S':
    print(f"Idade: {idade} anos")
  
    print("Estudante: Sim")
   
    print(f"Valor do ingresso: {meia}")

elif idade <= 12:
    print(f"Idade: {idade} anos")
 

    if estudante == 'S':
        print("Estudante: Sim")
       

    elif estudante == 'N':
        print("Estudante: Não")
       

    print(f"Valor do ingresso: {meia}")
    

elif idade >= 60:
    print(f"Idade: {idade} anos")
  

    if estudante == 'S':
            print("Estudante: Sim")
         
    elif estudante == 'N':
        print("Estudante: Não")
       

    print(f"Valor do ingresso: {meia}")

else:
    print(f"Idade: {idade} anos")
   
    print("Estudante: Não")
   
    print(f"Valor do ingresso: {ingresso}")
