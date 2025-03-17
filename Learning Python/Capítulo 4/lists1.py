# Listas são mutáveis. Podemos alterar valores de elementos da lista, e podemos adicionar e remover novos elementos.]
# Só podemos adicionar ao fim da lista.
# Mas podemos remover qualquer elemento da lista.
L10 = [10, 11, 12, 13]
print(L10)
L10.append(14) # acrescentar um 5o elemento
print(L10)
L10.pop(2) # remover o 3o elemento, isto é, o elemento "12"
print(L10)

# Listas aceitam múltiplos tipos simultaneamente.
print("\n", L10, sep = "")
L10 = [10, 11, 'O Grande Gatsby', 12, 13]
print(L10)
L10.append('Tudo é Rio') # acrescentar um 5o elemento
print(L10)

print()
lista = [123, 123,'Biologia Molecular', 3.14]
print(len(lista)) # 4
print(lista[2],end=" ") # Biologia Molecular
print(lista[-1]) # 3.14
print(lista[:-1]) # [123, 123, 'Biologia Molecular']
print(lista[:3]) # [123, 123, 'Biologia Molecular']
print(lista + ["Bruce", "Alexander", "Julian", "David"]) #[123, 123, 'Biologia Molecular', 3.14, 'Bruce', 'Alexander', 'Julian', 'David']
print(lista, ["Bruce", "Alexander", "Julian", "David"]) #[123, 123, 'Biologia Molecular', 3.14] ['Bruce', 'Alexander', 'Julian', 'David']
print(lista*2) #[123, 123, 'Biologia Molecular', 3.14, 123, 123, 'Biologia Molecular', 3.14]
print(lista) # [123, 123, 'Biologia Molecular', 3.14]
lista.append("Martin") # acrescenta um objeto ao fim da lista
print(lista) # [123, 123, 'Biologia Molecular', 3.14, 'Martin']
lista.pop(1) # remove o segundo elemento da lista
print(lista) # [123, 'Biologia Molecular', 3.14, 'Martin']

# método sort
lista = ["Bruce", "Alexander", "Julian", "David", "Martin", "Keith", "Peter"]
print(lista) # ['Bruce', 'Alexander', 'Julian', 'David', 'Martin', 'Keith', 'Peter']
lista.reverse() # inverte a ORDEM DOS ELEMENTOS na lista atual.
print(lista) # ['Peter', 'Keith', 'Martin', 'David', 'Julian', 'Alexander', 'Bruce']
lista.sort() # ordem alfabética por default.
print(lista) # ['Alexander', 'Bruce', 'David', 'Julian', 'Keith', 'Martin', 'Peter']
lista.sort(reverse=True) # ordem alfabética reversa.
print(lista) # ['Peter', 'Martin', 'Keith', 'Julian', 'David', 'Bruce', 'Alexander']
lista.sort(key=len) # ordem crescente de comprimento do elemento.
print(lista) # ['Peter', 'Keith', 'David', 'Bruce', 'Martin', 'Julian', 'Alexander']
lista.reverse() # inverte a ordem dos elementos na lista atual.
print(lista) # ['Alexander', 'Julian', 'Martin', 'Bruce', 'David', 'Keith', 'Peter']

# indexar fora do limite gera erro
# print(lista[100]) # IndexError: list index out of range
# lista[100]="Artmed" # IndexError: list assignment index out of range
