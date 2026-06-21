class carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def apresentar(self):
        print(f"Este é um {self.marca} do ano {self.ano}.")
        

carro1 = carro("Fiat", 2020)
carro1.apresentar()
carro2 = carro("Chevrolet", 2021)
carro2.apresentar()
