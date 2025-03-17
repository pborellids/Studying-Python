# strings são imutáveis; isto é, não é possível
# alterar seu valor a partir de cada posição individual de seus itens.
# Porém, é possível criar um novo objeto com o mesmo nome,
# e atribuir um novo valor a ele.
s = "computador"
print(s)

# Aqui ocorrerá um erro, pois não é possível alterar a string a partir de uma posição.
# s[0]="C" # TypeError: 'str' object does not support item assignment

# esse dará certo, pois estou criando um novo objeto "s",
# com a letra "C" concatenada com o restante da string anterior desde a segunda letra.
s = "C" + s[1:] 
print(s) # "Computador"

# podemos também converter a string em uma lista (e listas são mutáveis!)
s = "computador"
lista=list(s) # l é uma lista composta pelos caracteres de s.
print(lista) # "['c', 'o', 'm', 'p', 'u', 't', 'a', 'd', 'o', 'r']"
lista[0]="C" # é possível alterar uma posição específica de listas (mutabilidade)
print(lista) # ['C', 'o', 'm', 'p', 'u', 't', 'a', 'd', 'o', 'r']

# join: concatena as strings da lista utilizando uma string dada como separador. 
lista=''.join(lista)  # concatena as strings da lista, "separando os itens" com o caractere vazio.
print(lista) # "Computador" Pronto, recuperamos a string original, com o "C" maiúsculo que queríamos.

# é possível utilizar qualquer string como separador dos itens da string original.
lista='-.'.join(lista) 
print(lista) # "C-.o-.m-.p-.u-.t-.a-.d-.o-.r"
print("abc", "def", sep="./", end="")
print("_ghi")
lista=["tâmara", "uva", "limão", "abacate"]
print("//".join(lista))
print("'..'.join('xyz'): ", end = "")
print("..".join("xyz"), end = " - ") # a string "xyz" sendo tratada como lista pelo método join.
print('a string "xyz" sendo tratada como lista pelo método join.')