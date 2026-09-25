# Escreva uma função chamada valida_string que receba três
# parâmetros: uma string, um valor mínimo e um valor máximo.

# A função deve retornar True se o comprimento da string estiver entre o
# mínimo e o máximo (inclusive), e False caso contrário.

# Torne os parâmetros mínimo e máximo opcionais, com valores padrão de 1
# e 100, respectivamente.


def valida_string(string, minimo=1, maximo=100):
    tamanho = len(string)
    if minimo <= tamanho and tamanho <= maximo:
         return True
    else:
         return False

print(valida_string(input("Digite uma palavra: ")))
