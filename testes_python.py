transacoes = [
    {"tipo": "entrada", "valor": 1500.00},
    {"tipo": "saída", "valor": 200.00},
    {"tipo": "entrada", "valor": 800.00},
    {"tipo": "saída", "valor": 450.00},
]

def resumo_transacoes(transacoes):
    total_entrada = sum(tr["valor"] for tr in transacoes if tr["tipo"] == "entrada")
    total_saida = sum(tr["valor"] for tr in transacoes if tr["tipo"] == "saída")

    return {
        "total_entrada": total_entrada,
        "total_saida": total_saida,
        "saldo": total_entrada - total_saida
    }

print(resumo_transacoes(transacoes))







# def função, nome da função (oque ela recebe). : inicio da função
# variavel = regra pra armazenamento do valor, pode ser uma lista, dicionario, string, int, float, etc, no caso e um dicionario
# retorno da função, o que a função vai retornar, no caso um dicionario com os totais e saldo
# impresão no terminal do resultado da função, no caso o resumo das transações




# def resumo_transacoes(transacoes):    função
# if tr["tipo"] == "entrada":           condicional
# for tr in transacoes:                 loop
# class MinhaClasse:                    classe