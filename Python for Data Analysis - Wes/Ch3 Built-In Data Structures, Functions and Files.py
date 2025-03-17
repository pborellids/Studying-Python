# Revisão de estruturas de dados. Anotei as que eram novidades para mim.

# tuplas podem ser declaradas sem os parêntesis muitas vezes. 
# mas é melhor usar parêntesis por segurança.
from os import name


x = 4, 5, 6
print(type(x)) # <class 'tuple'>

# qualquer iterável pode ser convertido numa tupla usando a função tuple().
# Interáveis: string, list, dict, range, sets
print()
s = '456abc'
L = [4, 5, 6]
d = {'a':1, 'b': 2, 'c': 3}
r = range(3)
c = {4, 5, 6}
t1 = tuple(s)
t2 = tuple(L)
t3 = tuple(d)
t4 = tuple(r)
t5 = tuple(c)
print(type(s)) # <class 'str'>
print(type(L)) # <class 'list'>
print(type(d)) # <class 'dict'>
print(type(r)) # <class 'range'>
print(type(c)) # <class 'set'>
print(type(t1), t1) # <class 'tuple'> ('4', '5', '6', 'a', 'b', 'c')
print(type(t2), t2) # <class 'tuple'> (4, 5, 6)
print(type(t3), t3) # <class 'tuple'> ('a', 'b', 'c')
print(type(t4), t4) # <class 'tuple'> (0, 1, 2)
print(type(t5), t5) # <class 'tuple'> (4, 5, 6)

# tuplas são imutáveis. Entretanto, os elementos que sejam mutáveis podem ser mudados.
# aqui, vou incluir um novo elemento no segundo elemento da tupla.
print()
t = tuple([5, ['livro', 'título', 'altura'], True])
print(t[0]) # 5
print(t[1]) # ['livro', 'título', 'altura']
#t[0] = 3 # TypeError: 'tuple' object does not support item assignment
# t[1] = [1, 2, 3] # TypeError: 'tuple' object does not support item assignment
t[1].append('largura') # um novo elemento na lista
print(t) # (5, ['livro', 'título', 'altura', 'largura'], True)

# tuple unpacking 
print()
t1 = (4, 5, 6)
a, b, c = t1 # cada elemento da tupla vai pra respectiva variável.
# a, b, c, d = t1 # ValueError: not enough values to unpack (expected 4, got 3)
# a, b = t1 # ValueError: too many values to unpack (expected 2)
print(a, b, c) # 4 5 6
t2 = (4, 5, (6, 7))
a, b, (c, d) = t2 # mesmo tuplas com aninhamento podem ser unpacked.
print(a, b, c, d) # 4 5 6 7

# permutação FÁCIL de variáveis: 
print()
(x1, x2) = (1,2)
print(x1, x2) # 1 2 
(x2, x1) = (x1, x2)
print(x1, x2) # 2 1

# desempacotamento da sequência
print()
seq = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]
# 1a iteração: a=1, b=2, c=3. a,b,c recebem a primeira tupla da seq e assim por diante. Então a, b e c recebem 1, 2 e 3.
# uma forma concisa e inteligente de acessar os dados da coleção.
for a, b, c in seq: 
    print(a, b, c) 
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# cada elementos da coleção seq é lido e desempacotado. O elemento (1,2,3) é desempacotado em três valores (valor 1, valor 2, valor 3).
# e assim por diante. 
# esse "for" desempacota cada elemento da coleção seq em três valores separados.

print()
for a, b, c in seq:
# 1a iteração: a=1, b=2, c=3 etc. a,b,c recebem a primeira tupla da seq e assim por diante. Então a, b e c recebem 1, 2 e 3.
    print('a =', a, 'b =', b, 'c =', c)
# a = 1 b = 2 c = 3
# a = 4 b = 5 c = 6
# a = 7 b = 8 c = 9
# a = 10 b = 11 c = 12


# às vezes, queremos só desempacotar alguns dos valores da tupla. Nesse caso, usamos *rest (ou qualquer nome em seguida ao *)
# porque sempre é exigido que a quantidade de variáveis no lado esquerdo corresponda ao número de elemntos da coleção à direita.
# a variável rest será uma lista de comprimento livre.
print()
t = 1,2,3,4,5 # tupla com 5 elementos. Requeriria 5 variáveis para desempacotar.
# mas queremos desempacotar somente os dois primeiros elementos às variáveis a e b.
# *rest é uma forma de dizer que os outros três elementos vão nessa variável irrelevante. 
a, b, *rest = t # pronto. Não foi necessário atribuir a 5 variáveis. Com duaw, mais o *rest, já resolvemos.
print(a, b, rest) # 1 2 [3, 4, 5], e rest é uma lista.
a, b, *_ = t # muitos programadores utilizam "_" para variáveis irrelevantes.
print(a,b,_) # 1 2 [3, 4, 5], e _ é uma lista.
print(a,b) # 1 2

# o método count é interessante. Fornece a quantidade de ocorrências de um valor.
print()
a = (1,2,2,2,3,4,2)
print(a.count(2)) # 4

# listas: são criadas com [] ou com a função "list". São mutáveis.
print()
a_list = [2, 3, 7, None]
print(a_list)
tup = ('livro', 'mesa', 'cadeira')
b_list = list(tup)
print(b_list) # ['livro', 'mesa', 'cadeira']
b_list[1] = 'estante' 
print(b_list) # ['livro', 'estante', 'cadeira']
b_list.append('nicho')
print(b_list) # ['livro', 'estante', 'cadeira', 'nicho']
b_list.insert(1, 'divisória')
print(b_list) # ['livro', 'divisória', 'estante', 'cadeira', 'nicho']
print(b_list.pop(2)) # imprime estante e remove estante.
print(b_list) # ['livro', 'divisória', 'cadeira', 'nicho'] 
b_list.remove('divisória')
print(b_list) # ['livro', 'cadeira', 'nicho']
print('"cadeira" está em "b_list":', 'cadeira' in b_list) # True
print('"banco" está em "b_list":', 'banco' in b_list) # False

# construindo uma lista com um iterable
gen = range(10)
print(gen)
print(list(gen))

# concatenando listas
print()
print([4, 'páginas', None] + ['iPad', 'caneta', (2, 3)]) # [4, 'páginas', None, 'iPad', 'caneta', (2, 3)]

# ordenamento de listas
print()
L = ['serrote', 'escada', 'violão', 'alexa', 'notebook', 'livros', 'iPhone', 'mouse', 'controle']
L.sort()
print(L) # ['alexa', 'controle', 'escada', 'iPhone', 'livros', 'mouse', 'notebook', 'serrote', 'violão']
L.sort(key=len, reverse=True)
print(L) # ['controle', 'notebook', 'serrote', 'escada', 'iPhone', 'livros', 'violão', 'alexa', 'mouse']

# fatiamento (slicing) - slice 1:5 vai do elemento 1 (segundo elemento) até o elemento 4 (5o elemento). 
# A fatia 1:5 tem 5 - 1 = 4 elementos.
print()
L = [7, 2, 3, 7, 5, 6, 0, 1]
print('Lista:', L) # [7, 2, 3, 7, 5, 6, 0, 1]
# fatia 1:5 (4 elementos, do 2o ao 5o):
print('Fatia 1:5:', L[1:5]) # [2, 3, 7, 5]
# e podemos associar valores diretamente aos elementos de uma fatia.
L[3:5] = [0, 0]
print('Substituindo por 0 os elementos das posições 4 e 5:', L) # [7, 2, 3, 0, 0, 6, 0, 1]

# índices negativos fatiam a sequência a partir do fim.
# não é possível referir-se à ultima posição usando a notação de números negativos.
print()
L = [7, 2, 3, 7, 5, 6, 0, 1]
print('Lista:', L) # [7, 2, 3, 7, 5, 6, 0, 1]
print(L[-5:-2]) # [7, 5, 6]
print(L[-5:]) # [7, 5, 6, 0, 1] É a única forma de fazer a fatia ir até o último elemento.
               # Não é possível fazer uma referência negativa ao último elemento.
print(L[-5:-1]) # [7, 5, 6, 0]

# as fatias podem "pular" elementos de modo uniforme:
print()
L = [7, 2, 3, 7, 5, 6, 0, 1]
print('Lista:', L)
print('Elementos das posições pares da lista:', L[::2]) # [7, 3, 5, 0]
print('Elementos das posições ímpares da lista:', L[1::2]) # [2, 7, 6, 1]
print('Elementos espaçados de duas posições inicando na posição 0:', L[::3]) # [7, 7, 0]
print('Elementos espaçados de duas posições inicando na posição 1:', L[1::3]) # [2, 5, 1]

# [::-1] reverte a lista.
print('Lista em ordem reversa:', L[::-1])

# set vazio
set2=set() # set vazio

# dicionários
print()
d1 = {} # dicionário vazio
d1 = {'a': 'um valor', 'b': [1,2,3,4]}
print(d1) # {'a': 'um valor', 'b': [1, 2, 3, 4]}
d1['c'] = 'outro valor' # novo par chave-valor incluído.
print(d1) # {'a': 'um valor', 'b': [1, 2, 3, 4], 'c': 'outro valor'}
print(d1['b']) # [1, 2, 3, 4]
print('chave "b" existe no dicionário?', 'b' in d1) # True
print('chave "e" existe no dicionário?', 'e' in d1) # False
d1['d'] = 'mais um valor'
d1['e'] = 'um outro valor'
print(d1) # {'a': 'um valor', 'b': [1, 2, 3, 4], 'c': 'outro valor', 'd': 'mais um valor', 'e': 'um outro valor'}
del(d1['c']) # remove a chave 'c' e o valor associado a ela.
print(d1) # {'a': 'um valor', 'b': [1, 2, 3, 4], 'd': 'mais um valor', 'e': 'um outro valor'}

# removendo um valor do dicionário:
# valor_removido = d1.pop('b') # o pop REMOVE o valor, mas também RETORNA o valor removido.
# print('O elemento', valor_removido, 'foi removido do dicionário.') # O elemento [1, 2, 3, 4] foi removido do dicionário.
# Ou, mais econômico (remover + imprimir com um único comando):
print('O elemento', d1.pop('b'), 'foi removido do dicionário.') # O elemento [1, 2, 3, 4] foi removido do dicionário.
print(d1) # {'a': 'um valor', 'd': 'mais um valor', 'e': 'um outro valor'}

# os métodos keys(), values() e items() retornam iteráveis
# (e podem ser colocados no formato de listas, tuplas ou sets).
print(list(d1.keys())) # ['a', 'd', 'e'] Ordem original é mantida.
print(tuple(d1.keys())) # ('a', 'd', 'e') Ordem original é mantida
print(set(d1.keys())) # {'d', 'e', 'a'} Ordem original pode ser perdida.
print(list(d1.values())) # ['um valor', 'mais um valor', 'um outro valor']
print(tuple(d1.values())) # ('um valor', 'mais um valor', 'um outro valor')
print(set(d1.values())) # {'um outro valor', 'mais um valor', 'um valor'}
# adicionando um valor repetido ao dicionário. O print(set... só exibirá os valores distintos).
d1['f'] = 'um outro valor' # valor repetido da chave 'e'.
print(d1) # {'a': 'um valor', 'd': 'mais um valor', 'e': 'um outro valor', 'f': 'um outro valor'} 4 valores , 1 repetido.
print(set(d1.values())) # {'mais um valor', 'um valor', 'um outro valor'} 3 elementos apenas.
print(list(d1.items())) # [('a', 'um valor'), ('d', 'mais um valor'), ('e', 'um outro valor'), ('f', 'um outro valor')]

# atualizando o valor da chave f e incluindo novos pares chave-valor: g = valor g, h = valor h
d1.update({'g':'valor g', 'h':'valor h', 'f':'valor f'})
print(d1) # {'a': 'um valor', 'd': 'mais um valor', 'e': 'um outro valor', 'f': 'valor f', 'g': 'valor g', 'h': 'valor h'}

# zip: junta iteráveis em diversas tuplas ligando entre si os respectivos elementos dos iteráveis fornecidos.
print()
names = ['John', 'Alice', 'Bob', 'Lucy'] # iterável com nomes dos alunos
scores = [85, 90, 78, 92] # iterável com notas dos alunos
# zip(names, scores) # criaria 4 tuplas de 2 elementos:
#   Número da Tupla |     Tupla
#          1        |  ('John', 85)
#          2        |  ('Alice', 90)
#          3        |  ('Bob', 78)
#          4        |  ('Lucy', 92)]
# podemos converter as tuplas do zip em list, set e dict:
print(list(zip(names, scores))) # [('John', 85), ('Alice', 90), ('Bob', 78), ('Lucy', 92)]
print(set(zip(names, scores))) # {('Alice', 90), ('Lucy', 92), ('Bob', 78), ('John', 85)} ou outra ordem.
print(dict(zip(names, scores))) # {'John': 85, 'Alice': 90, 'Bob': 78, 'Lucy': 92}
# criando um dicionário pareando os elementos dos dois iteráveis originais:
print()
dic1 = {}
for chave, valor in zip(names, scores):
    dic1[chave] = valor
print(dic1) # {'John': 85, 'Alice': 90, 'Bob': 78, 'Lucy': 92}

# unindo duas listas em um dicionário (versão manual com método update({chave:valor}))
print()
dic2 = {}
for i in range(0,4):
    dic2.update({names[i] : scores[i]})
print(dic2) # {'John': 85, 'Alice': 90, 'Bob': 78, 'Lucy': 92}

# unindo duas listas em um dicionário (versão manual com chave-valor)
print()
dic3 = {}
for i in range(0,4):
    dic3[names[i]] = scores[i]
print(dic3) # {'John': 85, 'Alice': 90, 'Bob': 78, 'Lucy': 92}

# se o dicionário não tem um valor buscado, o get e o pop retornam "None" por default.
# mas é possível definir um valor alternativo para o retorno do get.
print('\n', dic3)
print('Testando a chave \'Peter\':', dic3.get('Peter')) # Retorno default. "None"
print(dic3.get('Peter', 'A chave \'Peter\' não existe.')) # Retorno forçado. "A chave 'Peter' não existe."
print('Removendo a chave \'John\':', dic3.pop('John')) # 85
print(dic3) # {'Alice': 90, 'Bob': 78, 'Lucy': 92} Par John:85 removido de dic3.
# print('Removendo a chave \'Peter\':', dic3.pop('Peter')) # KeyError: 'Peter'
print('Removendo a chave \'Peter\':', dic3.pop('Peter', 'Chave \'Peter\' não existe.'))

# exercício de listar palavras em um dicionário conforme suas iniciais. As palavras virão de uma lista.
# isto aqui:
# lista: ['manga', 'alface', 'beterraba', 'melancia', 'abacate', 'banana']
# dicionário: {'m': ['manga', 'melancia'], 'a': ['alface', 'abacate'], 'b': ['beterraba', 'banana']}
print()
palavras = ['manga', 'alface', 'beterraba', 'melancia','abacate', 'banana']
print(palavras)
por_inicial = {}
for palavra in palavras:
    inicial = palavra[0]
    if inicial not in por_inicial:
        por_inicial[inicial] = [palavra]
    else:
        por_inicial[inicial].append(palavra)
print(por_inicial)

