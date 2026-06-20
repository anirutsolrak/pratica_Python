produto ={
    "nome": "livro",
    "valor": 25.50,
    "qtd": 3
}


try:
    produto = (produto["nome"], produto["email"])  
    print(produto)
except:
    print("deu erro")