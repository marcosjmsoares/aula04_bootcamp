# Exercícios de Listas e Dicionários
# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros = list(range(1,11))
# for numero in numeros:
#     print(numero**2)

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# from typing import Dict, Any

# livro1: Dict[str, Any] = {
#     "Titulo":"Game of Thrones",
#     "Autor": "Estagiario",
#     "Ano": 2005
# }

# livro2: Dict[str, Any] = {
#     "Titulo":"Game of Thrones 2",
#     "Autor": "Estagiario",
#     "Ano": 2007
# } 

# lista_de_livros = []

# lista_de_livros.append(livro1)
# lista_de_livros.append(livro2)

# print(lista_de_livros)

# lista_de_elementos: list = livro.items()
# for elemento in lista_de_elementos:
#     print(elemento)

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compras = ["maçã", "banana", "cereja", "pera"] 
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65,"pera":1.00}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}") 