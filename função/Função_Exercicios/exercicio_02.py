# Crie uma função chamada soma_imposto que possua dois
# parâmetros:

def soma_imposto(taxa_imposto, custo):
    taxa_decimal = taxa_imposto / 100
    imposto = custo * taxa_decimal
    return custo + imposto

custo_valor = (float(input("valor do produto: ")))
taxa_valor = (float(input("valor da taxa: ")))
resultado = soma_imposto(taxa_valor, custo_valor)

print (f"Seu valor com a taxa: {resultado:.2f}")
