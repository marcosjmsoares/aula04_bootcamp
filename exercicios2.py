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
lista_idade:list = [10,20,30,14,15,13,25]
lista_maior_18:list = [idade for idade in lista_idade if idade >= 18]
    
print(lista_maior_18)


# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [{"nome":"maria","idade":"22"},
           {"nome":"rhassan","idade":"39"},
           {"nome":"thiago","idade":"26"},
           {"nome":"thales","idade":"17"},
           {"nome":"marcos","idade":"33"}]
pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)


# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.



# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.




# Exercícios com Dicionários
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.


# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.



# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.


# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

