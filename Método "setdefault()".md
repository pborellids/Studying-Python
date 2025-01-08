# O método "setdefault()" em dicionários

O método ```setdefault()``` faz simultaneamnete duas operações: ele verifica se existe uma determinada chave no dicionário (que é formado por pares chave-valor).<br/>
Se existir, então ele atualiza o valor associado à chave.<br/>
Caso a chave não exista, a chave é criada e pareada com o valor fornecido.<br/>
Exemplo:<br/>
chaves = ['objeto', 'material', 'preço'] # lista com chaves que serão usadas on dicionário
valores = ['mesa', 'madeira', '1.000,00'] # lista com valores que serão usados no dicionário
dic1 = {} # criação de dicionário vazio
for i in range(3): # i variando de 0 a 2 inclusive
    dic1.setdefault(chaves[i], valores[i]) # como nenhuma das chaves existe,
                                           # será criado o par chave-valor com os dados das posições homólogas das duas listas.
print(dic1) # {'objeto': 'mesa', 'material': 'madeira', 'preço': '1.000,00'}
