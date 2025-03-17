x = set('abcdeeeeeeeeeeeeeeeeeeeeeeee')
y = set("bdxyz")
print(x) # {'a', 'd', 'c', 'b', 'e'}
print(y) # {'y', 'd', 'x', 'b', 'z'}
print(x-y) # diferença entre os conjuntos x e y. Equivale a x excluída a intersecção com y. {'c', 'a', 'e'}
print(x | y) # união de x e y. {'a', 'y', 'd', 'c', 'x', 'b', 'e', 'z'}
print(x & y) # intersecção entre x e y. {'d', 'b'}
print('diferença simétrica:', x^y) # diferença simétrica. Só que x e y têm de diferente entre si. {'a', 'x', 'c', 'y', 'e', 'z'}
x2 = set('de')
print(x>x2) # x contém x2, ou x2 está contido em x = True
print(x>y) # x contém y = false
print(x<y) # x está contido em y = false

# in faz um search no iterável. "in" = "pertence a".
print()
print('e' in x) # true
print('e' in y) # false
print('e' in 'escola') # true
print('e' in [1, 2, 'e', 7.5]) # true
print('e' in [1, 2, 'escola', 7.5]) # false

# métodos dos conjuntos
print()
z = x.intersection(y)
print(z) # {'b', 'd'}
z.add('livro')
print(z) # {'b', 'd', 'livro'}
z.update(set(['PAPEL', 'ROTEADOR'])) # adicionar os elementos 'PAPEL' e 'ROTEADOR' a z.
print(z) # {'b', 'PAPEL', 'd', 'ROTEADOR', 'livro'}
z.remove('d')
print(z) # {'livro', 'b', 'PAPEL', 'ROTEADOR'}

# sets são iterable. Por isso, podem ser utilizados em list comprehensions e loops. E suportam o método len.
# porém, não são ordenados. Por isso, não suportam índices nem slices.
print()
for item in z:
    print(item * 3)
# livrolivrolivro
# PAPELPAPELPAPEL
# ROTEADORROTEADORROTEADOR
# bbb

# sets podem ser criados apenas com {} ou comando "set".
# sets podem ser vistos como "keyless" dictionaries (daí os curly braces).
print()
x = (1,2,3)
print(type(x)) # <class 'tuple'>
x = {1,2,3}
print(type(x)) # <class 'set'>
x = set([1,2,3])
print(type(x)) # <class 'set'>

# sets são muttable:
print()
x = {1,2,3}
print(x) # {1, 2, 3}
x.add(4)
print(x)# {1, 2, 3, 4}

# o set vazio só pode ser criado com o comando "set". As literais {} são úteis na criação de sets não vazios.
print()
y = {} # tentando criar um set vazio. Mas Python o considera um dicionário vazio.
print(y, type(y)) # {} <class 'dict'>
y = set() # set vazio
print(y, type(y)) # set() <class 'set'>

# a impressão de um conjunto vazio se dá um pouco diferente, porque {} seria um dicionário vazio.
print()
x = {1,2,3,4}
print(x) # {1, 2, 3, 4}
y = x - {1,2,3,4}
print(y, type(y)) # set() <class 'set'>

# inicializando um set vazio
print()
x = set()
print(x) # set()
x.add(1.78)
print(x) # {1.78}

# é possível operar sets e outros iterables usando os métodos dos sets
# essas operações seriam impossíveis com os operadores.
print()
# {1,2,3} | [3,4] # gera erro TypeError: unsupported operand type(s) for |: 'set' and 'list'
print({1,2,3}.union([3,4])) # {1, 2, 3, 4} União do set com list
print({1,2,3}.union({3,4})) # {1, 2, 3, 4} União de set com set
print({1,2,3}.union(set([3,4]))) # {1, 2, 3, 4} União de set com set
print({1,2,3}.intersection((1,3,5))) # {1, 3} Intersecção de set com tuple
print({1,2,3}.issubset(range(-1,4))) # True - set está contido no iterable range

# sets são mutable, mas apenas no sentido de que podem ser expandidos e reduzidos.
print()
x = {1.55}
print(x)
# x.add([1,2,3]) # Lista é mutable (unhashable, elementos podem mudar), mas set é hashable (elementos não podem ser mudados).
                 # TypeError: unhashable type: 'list'
x.add((1,2,3)) # tuples são imutáveis/hashable. Só podemos acrescentar elementos hashable a um set.
print(x) # {1.55, (1, 2, 3)}
x |= {(4,5,6), (1,2,3)}
print(x) # {1.55, (1, 2, 3), (4, 5, 6)}

# membresia (pertencimento):
print((1,2,3) in x) # True
print((1,4,3) in x) # False
