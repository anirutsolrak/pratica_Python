numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def nova_lista(numeros):
    return [numeros_maiores for numeros_maiores in numeros if numeros_maiores > 5]
print(nova_lista(numeros))




#podemos fazer sem passar parametro assim ele passar a aceitar qualquer coisa ma pratica mas funciona precisa ser a variavel global se não não funciona
def nova_lista():
    return [numeros_maiores for numeros_maiores in numeros if numeros_maiores > 5]
#print(nova_lista())