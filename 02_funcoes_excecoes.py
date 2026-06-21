#Problema 2 — Funções e exceções
#Você tem uma função que calcula o rendimento de um investimento. Se o valor inicial for zero ou negativo, deve lançar um erro com uma mensagem clara. Se a taxa for negativa, também deve lançar erro.
#Entrada esperada:
#pythoncalcular_rendimento(1000.00, 0.05, 12)  # valor, taxa mensal, meses
#Saída esperada:
#python1795.86  # valor final arredondado em 2 casas

#Solução:

def calcular_rendimento(valor_inicial, taxa_mensal, meses):
    if valor_inicial <= 0:
        raise ValueError("Valor inicial deve ser maior que zero")
    if taxa_mensal < 0:
        raise ValueError("Taxa mensal não pode ser negativa")
    
    valor_final = valor_inicial * (1 + taxa_mensal) ** meses
    return round(valor_final, 2)

print(calcular_rendimento(1000.00, 0.05, 12))