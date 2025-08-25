# Exercícios de Listas e Dicionários resolvidos
# Resoluções de Listas e Dicionários
# 1. Lista de números ao quadrado
# numeros = list(range(1, 11))
# for numero in numeros:
#     print(numero**2)

# 2. Modificar lista de linguagens
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

# 3. Informações de um livro
# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")

# 4. Contar ocorrências de caracteres
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

# 5. Preço total da lista de compras
# lista=[123.45,10.44,10.99]
# soma:int = 0
# for valor in lista:
#     soma += valor

# print(soma)

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
# lista_email:list = ["marcos@gmail.com", "david@gmail.com", "marcos@gmail.com"]
# emails_unicos = list(set(lista_email))

# print(emails_unicos)


# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# lista_idade:list = [10,20,30,14,15,13,25]
# lista_maior_18:list = [idade for idade in lista_idade if idade >= 18]
    
# print(lista_maior_18)


# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [{"nome":"maria","idade":"22"},
#            {"nome":"rhassan","idade":"39"},
#            {"nome":"thiago","idade":"26"},
#            {"nome":"thales","idade":"17"},
#            {"nome":"marcos","idade":"33"}]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])
# print(pessoas)


# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
# lista=[123.45,10.44,10.99,15,123,23]
# soma:int = 0
# quant:int = 0
# for valor in lista:
#     soma += valor
#     quant += 1
# print(soma/quant)


# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# lista_valores = range(10)
# lista_par = [par for par in lista_valores if par % 2 == 0]
# lista_impar = [par for par in lista_valores if par % 2 == 1]

# print(f"Pares: {lista_par}, Impares: {lista_impar}")


# Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# lista_produtos = [{"nome": "TV", "preco": "1500"},
#                   {"nome": "Airfry", "preco": "500"},
#                   {"nome": "Notebook", "preco": "3500"},
#                   {"nome": "Geladeira", "preco": "5500"},
#                   {"nome": "Fogão", "preco": "700"}
#                   ]

# for produto in lista_produtos:
#     if produto["nome"] == "Notebook":
#         produto["preco"] = 4000

# print(lista_produtos)        

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
# dicionario1 = {"nome": "TV", "preco": "1500"}
# dicionario2 = {"nome2": "Airfry", "preco2": "500"}

# dicionario_fundido = {**dicionario1, **dicionario2}

# print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# lista_produtos = [{"nome": "TV", "quantidade": 0},
#                   {"nome": "Airfry", "quantidade": 5},
#                   {"nome": "Notebook", "quantidade": 0},
#                   {"nome": "Geladeira", "quantidade": 0},
#                   {"nome": "Fogão", "quantidade": 15}
#                   ]

# lista_com_estoque = []

# for produto in lista_produtos:
#     if produto["quantidade"] > 0:
#         lista_com_estoque += produto
#         print(produto)
  

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a":1,"b":2,"c":3}

chaves = list(dicionario.keys())
valores = list(dicionario.values())

print(f"Chaves: {chaves}")
print(f"Valores: {valores}")

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

