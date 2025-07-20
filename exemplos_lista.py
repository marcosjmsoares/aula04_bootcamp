# numeros = []
# numeros.extend(range(0,5))
# print(numeros)
import json

lista = ["sapato", 39, 10.38, True]

produto_01: dict = {
    "nome":"sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True
}

produto_02: dict = {
    "nome":"Televisao",
    "quantidade":10,
    "preco":70.38,
    "disponibilidade":True
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)