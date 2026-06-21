from fastapi import FastAPI




vestuario = [{'nome': "Camiseta", 'preco': 50.00, 'id': 1},
             {'nome': "Calça", 'preco': 100.00, 'id': 2},
             {'nome': "Tênis", 'preco': 150.00, 'id': 3},
             {'nome': "Jaqueta", 'preco': 200.00, 'id': 4},
             {'nome': "Vestido", 'preco': 250.00, 'id': 5}]


app = FastAPI()

@app.get("/vestuario")
def produtos():
    return vestuario

@app.get("/vestuario/{id}")
def produtos(id: int):
    for item in vestuario:
        if item["id"] == id:
            return item
    return {"message": "Produto não encontrado"}

 