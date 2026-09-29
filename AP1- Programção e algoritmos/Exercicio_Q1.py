#Demonstrar passo-a-passo a resolução das duas expressões abaixo (como
#visto em aula):
#Considerar: a = 15, b = 4 e c = 2
#res_1 = a / b - c ** b % a + a // b % 5
#res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)



#res_1 = 15/4 - 2 ** 4 % 15 + 15 // 4 % 5
#res_1 = 15/4 - 16 % 15 + 15 // 4 % 5
#res_1 = 3.75 - 1 + 3
#res_1 = 5.75

a = 15
b = 4 
c = 2


res_1 = a / b - c ** b % a + a // b % 5

print(res_1)



#res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)
#res_2 = not (2 == 0) and (16 + 2 > 15 or 15 - 16 != 7)
#res_2 = not (2 == 0) and (18 > 15 or -1 != 7)
#res_2 = not (false) and (True or True)
#res_2 = false and True
#res_2 = false

res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)

print(res_2)