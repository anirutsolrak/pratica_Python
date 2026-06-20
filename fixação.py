def saudacao (nome):
    return f"Olá, {nome}! Bem-vindo ao Python!"
#print(saudacao("carlos"))

numeros = [1, 2, 3, 4, 5]

def valores(numeros):
    for numero in numeros:
        if numero % 2 == 0:
            print(f"{numero} é par")

#print(valores(numeros)) 
#print(valores([5, 6, 8, 15]))

Pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo",
    "email": "carlos@email.com"
}

def apresentar_pessoa(pessoa):
    return f"Ola, meu nome é {pessoa['nome']}, tenho {pessoa['idade']} anos, moro em {pessoa['cidade']} e meu email é {pessoa['email']}."

#print(apresentar_pessoa(Pessoa))

converter = "abc"
try:
    teste = int(converter)
except:
 #   print(f"valor, \"{converter}\", não é um numero")


 class animal:
     def __init__(self, especie, idade):
         self.especie = especie
         self.idade = idade

     def descrever(self):
        return f"esta(e) é um {self.especie} com {self.idade} anos de idade."
     
animal1 = animal("cachorro", 5)
#print(animal1.descrever())

lista = [1, 2, 3, 4, 5]

def lista_impar(lista):
    return [impar for impar in lista if impar % 2 != 0]
#print(lista_impar(lista))

texto = "Olá, mundo! Bem-vindo ao Python."

def formatar(texto):
    return texto.strip().replace("Python", "é o tchan ").upper()

#print(formatar(texto))
