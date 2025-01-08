# O método "setdefault()" em dicionários

## O que faz
O método ```setdefault()``` faz simultaneamente duas operações: ele verifica se existe uma determinada chave no dicionário (que é formado por pares chave-valor).<br/>
* Se existir, então ele atualiza o valor associado à chave.<br/>
* Caso a chave não exista, a chave é criada e pareada com o valor fornecido.<br/>
## Exemplo 1:<br/>
Será criado um dicionário com os dados das posições homólogas das listas "chaves" e "valores".<br/> 
```python
chaves = ['objeto', 'material', 'preço'] # lista com chaves que serão usadas on dicionário
valores = ['mesa', 'madeira', '1.000,00'] # lista com valores que serão usados no dicionário
dic1 = {} # criação de dicionário vazio
for i in range(3): # i variando de 0 a 2 inclusive
    dic1.setdefault(chaves[i], valores[i]) # como nenhuma das chaves existe,
                                           # será criado o par chave-valor com os dados das posições homólogas das duas listas.
print(dic1) # {'objeto': 'mesa', 'material': 'madeira', 'preço': '1.000,00'}
```
<br/>
## Exemplo 2:<br/>
Numa aplicação mais interessante, e um pouco mais complexa, vamos criar um dicionário organizado (chaves) pelas iniciais das palavras de uma lista.<br/>

A lista de palavras e o dicionário que buscamos são:<br/>
```python
palavras = ['manga', 'alface', 'beterraba', 'melancia','abacate', 'banana']
# dicionário organizado pelas iniciais das palavras:
{'m': ['manga', 'melancia'], 'a': ['alface', 'abacate'], 'b': ['beterraba', 'banana']}
```
<br/>

### Implementação:<br/>
```python
palavras = ['manga', 'alface', 'beterraba', 'melancia','abacate', 'banana'] # lista original de palavras
print(palavras) # ['manga', 'alface', 'beterraba', 'melancia', 'abacate', 'banana']
por_inicial = {} # dicionário vazio
for palavra in palavras:
    inicial = palavra[0] # somente as letras iniciais são obtidas
    por_inicial.setdefault(inicial, []).append(palavra) # key = inicial, value = lista de palavras com a inicial
print(por_inicial) # {'m': ['manga', 'melancia'], 'a': ['alface', 'abacate'], 'b': ['beterraba', 'banana']}
```
