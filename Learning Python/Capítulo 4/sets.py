# sets são uma adição recente ao Python. São utilizados através do comando "set" ou da notação {}.
# São como dicionários vazios, com apenas as chaves.
# Sets são realmente tratados como conjuntos em Python. Descartam repetições de elementos.
# Sets não garantem a ordem, e são immutable (mas é possível adicionar e remover valores).

set1 = set('independência')
print("set1 =", set1) # {'a', 'e', 'i', 'd', 'p', 'n', 'c', 'ê'}
print(len(set1)) # 8
print(len('independência')) # 13

set2 = {'i', 'n', 'd', 'e', 'p', 'e', 'n', 'd', 'ê', 'n', 'c', 'i', 'a'}
print()
print("set2 =", set2) # {'p', 'a', 'n', 'i', 'e', 'ê', 'c', 'd'}
print(len(set2)) # 8
print(len('independência')) # 13

print()
print((set1,set2)) # ({'c', 'p', 'e', 'ê', 'd', 'a', 'n', 'i'}, {'c', 'p', 'e', 'ê', 'd', 'a', 'n', 'i'})
print(set1,set2) # {'c', 'p', 'e', 'ê', 'd', 'a', 'n', 'i'} {'c', 'p', 'e', 'ê', 'd', 'a', 'n', 'i'}

print()
set3 = set('Amapá')
print("set3 = ", set3) # set3 =  {'m', 'A', 'a', 'p', 'á'}
print('n(set3):', len(set3)) # 5
set4 = set('Amazonas') 
print('set4 = ', set4) # set4 =  {'m', 'A', 'a', 'z', 'o', 'n', 's'}
print('n(set4):', len(set4)) # 7
print(set3 & set4) # intersecção {'a', 'm', 'A'} # 3
print('n(interseção) set3 & set4:', len(set3 & set4))
print(set3 | set4) # união {'n', 'm', 'á', 'a', 'p', 'z', 'A', 'o', 's'}
print(len(set3 | set4)) # 9 (como esperado pela teoria de conjuntos: 5 + 7 - 4)
print('Diferença set3 - set4:', set3 - set4)

# set compreehension
print({n ** 2 for n in [3, 4, 5, 6]})

# sets podem ser utilizados para coisas bem interessantes:
# 1) remover duplicações de uma lista: convertemos a lista para um set e, em seguida, de volta para uma lista.
#    a ordem pode mudar no fim, claro.
print(list(set([1,2,3,4,4,3,1,1,5,10]))) # temos a lista sem repetiçoes [1, 2, 3, 4, 5, 10]
# 2) calcular a diferença entre duas sequências:
print(set('escola') - set('bola')) # {'s', 'e', 'c'}
# 3) verificar se são idênticos (sem considerar a ordem):
print(set('amor') == set('roma')) # True

print()
print('e' in set('escola')) # True. Sets aceitam o "in".

# sets são immutable. Entretanto, é possível acrescentar e remover novos elementos.
# apenas não se pode alterar elementos existentes.
myset1 = {1,2,3,4} # set com 4 elementos
print(myset1) # {1, 2, 3, 4}
myset1.add(5) # adicionar o elemento "5"
print(myset1) # {1, 2, 3, 4, 5}
myset1.remove(2) # remover o elemento "2"
print(myset1) # {1, 3, 4, 5}
