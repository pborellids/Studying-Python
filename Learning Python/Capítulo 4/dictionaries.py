# Dicionários não são sequências. São classificados como "mapping".
# Mappings incluem "keys" que rotulam os próprios dados, e são mutáveis.
# A referência a um elemento é feita como nas listas, porém usando as keys, não posições.
# Até a 3.5, dicionários não mantinham a ordem das chaves.
# A partir da 3.6, e ficou garantido na 3.7, diconários guardam a ordem de chaves utilizada na criação.
D1 = {'objeto': 'carregador', 'quantidade': '1', 'cor': 'preto'}
print(D1)
print(D1['objeto'])
print(D1['quantidade'])
print(D1['cor'])

# Dicionários podem ser expandidos e reduzidos localmente, ao contrário de listas,
# que não permitem referências além de seus limites iniciais.
D2 = {}
D2['Título'] = 'Nexus'
D2['num_pag'] = '497'
D2['Autor'] = "Yuval Noah Harari"
print(D2)
print(D2['Autor'])

# Dicionários também podem ser criados utilizando o "dict" type name.
D3 = dict(Título = 'Matemática Financeira', num_pag = '440', Autor = 'Abelardo de Lima')
print(D3)
print(D3['num_pag'], 'páginas.')

# E também é possível criar dicionários com "zip", após ler arquivos csv por exemplo.
D4 = dict(zip(['Título', 'num_pag', 'Autor'], ['O Xangô de Baker Street', '189', 'Jô Soares']))
print(D4)
print(D4['Título'])

# As chaves passaram a garantir a ordem dos valores retornados na 3.7. 
# Porém, tem que testar entre execuções do programa.
# Com chaves, saem assim: {'a': '123', 'b': '456'} (execute o programa mais de uma vez)
print({'a':'123','b':'456'})
print({'a':'123','b':'456'})
print({'a':'123','b':'456'})
print({'a':'123','b':'456'})

# Sem chaves, a ordem muda entre as execuções do programa.
# Num dicionário sem chaves, os elementos podem sair {'456', '123'} na 1a execução e {'123', '456'} na segunda.
print({'123','456'})
print({'123','456'})
print({'123','456'})
print({'123','456'})

# Dicionários podem ser estruturas bem flexíveis. Podemos utilizar nesting para elaborar melhor a estrutura dos dados.
# E o nesting pode ser feito com outro dicionário, uma lista etc.
# No nesting com uma lista, é possível expandir a lista (append) se necessário.
D5 = {'Título': {'Principal': 'Álgebra Linear', 'Subtítulo': 'com Aplicações'},
      'Divisões': {'Capítulos': 10, 'Apêndices': 2},
      'Tópicos': ['Sistemas de Equações Lineares e Matrizes', 'Determinantes', 'Espaços Vetoriais Euclidianos'],
      'Editora': 'Bookman'}
print(D5)
# {'Título': {'Principal': 'Álgebra Linear', 'Subtítulo': 'com Aplicações'}, 
# 'Divisões': {'Capítulos': 10, 'Apêndices': 2}, 
# 'Tópicos': ['Sistemas de Equações Lineares e Matrizes', 'Determinantes', 
# 'Espaços Vetoriais Euclidianos'], 
# 'Editora': 'Bookman'}
print(D5['Título']) # {'Principal': 'Álgebra Linear', 'Subtítulo': 'com Aplicações'}
print(D5['Título']['Principal'],D5['Título']['Subtítulo']) # Álgebra Linear com Aplicações

# dicionários são mutáveis. Podemos incluir novas chaves e valores.
D5['Estante'] = 'Nicho N3'
print(D5)
# {'Título': {'Principal': 'Álgebra Linear', 'Subtítulo': 'com Aplicações'}, 'Divisões': {'Capítulos': 10, 'Apêndices': 2},
#  'Tópicos': ['Sistemas de Equações Lineares e Matrizes', 'Determinantes', 'Espaços Vetoriais Euclidianos'], 
# 'Editora': 'Bookman', 'Estante': 'Nicho N3'}

# Como sequências são mutáveis, podemos adicionar mais um tópico a ela.
# Basta fazer uma referência à lista e utilizar o método .append.
D5['Tópicos'].append('Espaços Vetoriais Arbitrários')
print(D5)
# {'Título': {'Principal': 'Álgebra Linear', 'Subtítulo': 'com Aplicações'}, 
# 'Divisões': {'Capítulos': 10, 'Apêndices': 2}, 
# 'Tópicos': ['Sistemas de Equações Lineares e Matrizes', 'Determinantes', 
# 'Espaços Vetoriais Euclidianos', 'Espaços Vetoriais Arbitrários'], 
# 'Editora': 'Bookman'}

# Verificar se a chave "Data" existe no dicionário:
print('Data' in D5) # False
print('Editora' in D5) # True


# # Missing Keys: If. É possível testar se uma determinada chave existe ou não no dicionário.
# Se houver aninhamento, é preciso testar no aninhamento, não no dicionário.

# Se Key estiver na estrutura principal de D5:
print()
key = "Divisões"
resposta = key + ' não está em D5.'
if key in D5:
      resposta = key + ' está em D5.' + "\n"
      resposta = resposta + 'Por hoje é só!' + "\n"
print(resposta)

# Se Key estiver num aninhamento de D5:
key = "Principal"
resposta = key + ' não está em D5.'
if key in D5['Título']: # indicando o primeiro aninhamento, feito na chave 'Título'
      resposta = key + ' está na chave "Título."' + "\n"
      resposta = resposta + 'Por hoje é só!'
print(resposta)

# Consulta das chaves do dicionário:
print(D5.keys()) # dict_keys(['Título', 'Divisões', 'Tópicos', 'Editora', 'Estante'])

# Um set é um "dicionário sem keys" e não oferece o método .keys()
S1 = {'123', 'abc'}
#    print(S1.keys())
#          ^^^^^^^
#AttributeError: 'set' object has no attribute 'keys'

# Reordenando a organização do dicionário
D6 = {"Área": "Física", "Título": "University Physics", "Autor": "Young and Freedman"}
print("\n", D6, sep = "")
Ks = list(D6.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
      print(key, "=>", D6[key])

# Reordendando com uso da função "sorted":
D6 = {"Área": "Física", "Título": "University Physics", "Autor": "Young and Freedman"}
print("\n", D6, sep = "")
for key in sorted(D6):
      print(key, "=>", D6[key])
