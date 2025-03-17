from math import sqrt

# Python não tem ferramentas built-in para matrizes. Mas é possível simular algumas situações de matrizes
# utilizando "aninhamento" (nesting) de listas (isto é, listas de listas, sendo que a lista "de fora" 
# representa a matriz, e as listas de dentro representam as linhas da matriz.
# Com nesting, é possível escrever a atribuição em múltiplas linhas do código fonte. 
matriz = [[1, 2, 3], # matriz 3x3.
          [4, 5, 6],
          [7, 8, 9]]
print(matriz) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1]) # segunda linha: [4, 5, 6]
print(matriz[1][2]) # segunda linha, terceiro elemento: 6

# Mas como recuperar uma coluna inteira?
# Como a matriz é armazenada em uma linha apenas (é como o nesting funciona),
# ficamos sem um jeito de nos referir a uma coluna.
# O TRUQUE para recuperar uma coluna:
# recupere o segundo elemento ("segunda coluna") de cada elemento da matriz.
# mas cada elemento da matriz é uma linha da matriz.
# recuperar o segundo elemento de cada linha acaba levando a recuperação de toda a segunda coluna da matriz.
print([linha[1] for linha in matriz]) # cada elemento é chamado de "linha" [2, 5, 8].
print([linha[1] + 3 for linha in matriz]) # somando 3 a cada elemento da 2a coluna [5, 8, 11].
print([linha for linha in matriz]) # cada elemento da lista matriz é uma linha da matriz [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz) # matriz na forma nativa (sequência) [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\n", matriz[0], sep = "") # primeira linha da matriz [1, 2, 3]
print(matriz[1]) # segunda linha da matriz [4, 5, 6]
print(matriz[2]) # terceira linha da matriz [7, 8, 9]
# Resultando em:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

print("\n", [linha[1] for linha in matriz if linha[1] % 2 == 0], sep = "") # elementos pares da segunda coluna na matriz [2, 8]
print([matriz[i][i] for i in [0,1,2]]) # diagonal principal da matriz [1, 5, 9]

# dobrando os caracteres de cada elemento de uma sequência
print([c*2 for c in "Introduction"]) # ['II', 'nn', 'tt', 'rr', 'oo', 'dd', 'uu', 'cc', 'tt', 'ii', 'oo', 'nn']

# List Comprehensions are powerful
L2 = list(range(2,6))
print(L2) # [2, 3, 4, 5]
print([[x ** 2, x ** 3] for x in L2]) # [[4, 8], [9, 27], [16, 64], [25, 125]]
L3 = list(range(-10,7,3))
print(L3) # [-10, -7, -4, -1, 2, 5]
print([[x, x**2, sqrt(x), x/2] for x in L3 if x > 0]) # [[2, 4, 1.4142135623730951, 1.0], [5, 25, 2.23606797749979, 2.5]]

# soma de cada linha da matriz
print(sum(matriz[0])) # 6
print(sum(matriz[1])) # 15
print(sum(matriz[2])) # 24
print([sum(matriz[i]) for i in [0, 1, 2]]) # [6, 15, 24]

# soma de todas as linhas da matriz
print(sum([sum(matriz[i]) for i in [0, 1, 2]])) # 45
