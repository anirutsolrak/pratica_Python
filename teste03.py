numeros = [1, 2, 3, 4, 10, 6, 8, 5]

def valores(numeros):
    for numero in numeros:
        if numero > 4:
            print(numero)
        else:
            print("numero menor que 4")
(valores(numeros))