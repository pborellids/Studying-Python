# tuples são como sequências, mas são immutable.
# Tuplas suportam muito menos métodos que listas.
# A vantagem de tuplas sobre listas é que elas garantem que os dados que carregam não mudarão.

T = (1, 2, 3, 4)
print(len(T)) # 4

print(T + (5, 6, 4)) # (1, 2, 3, 4, 5, 6, 4)

T += (5, 6, 4) # (1, 2, 3, 4) => (1, 2, 3, 4, 5, 6, 4) 
print(T)

print(T[0]) # 1

print(T.index(3)) # 2. O valor "3" está na posição 2.

print(T.count(4)) # 2. O elemento "4" aparece duas vezes na tupla T.

# Concatenando uma nova tupla (10, 20) com a tupla anterior:
T = (10, 20) + T[1:] 
print(T) # (10, 20, 2, 3, 4, 5, 6, 4) 

T2 = (100) # Isso aqui declara um inteiro (que apenas está entre parêntesis). É equivalente a T2 = 100. 
print('T2 = (100): ', 'tipo: ', type(T2), ', inteiro cujo valor é ', T2, ".", sep = "")
# T2 = (100): tipo: <class 'int'>, inteiro cujo valor é 100.

T2 = (100,) # Isso declara uma tupla de um único termo.
print('T2 = (100,): ', 'tipo: ', type(T2), ', tupla ', T2, ".", sep = "") 
# T2 = (100,): tipo: <class 'tuple'>, tupla (100,).

# concatenando a tupla de um valor apenas (100,) ao início da tupla T. 
T = (100,) + T[1:]
print(T) # (100, 20, 2, 3, 4, 5, 6, 4)

# Tuplas podem ser declaradas sem os parêntesis, se não houver risco de confusão.
T = 100, 200, 300, 1000
print(T) # (100, 200, 300, 1000)

# tuplas podem guardar tipos misturados:
T = 100, "abcd", [1, 3, 5, 7] 
print(T) # (100, 'abcd', [1, 3, 5, 7])
print(T[1]) # abcd
print(T[2]) # [1, 3, 5, 7]
print(T[2][3]) # 7

# tuplas são imutáveis. Impossível utilizar append.
# T.append(50) # AttributeError: 'tuple' object has no attribute 'append'
