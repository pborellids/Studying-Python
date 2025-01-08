# O método "setdefault()" em dicionários permite a criação de dicionários a partir de pares de listas.

## O que faz
O método ```setdefault()``` faz simultaneamente duas operações: ele verifica se existe uma determinada chave no dicionário (dicionários são formados por pares chave-valor). O mnétodo retorna o valor associado à chave.<br/>
* Se a chave existir no dicionário, então o método atualizará o valor já associado à chave, e retornará o respectivo novo valor.<br/>
* Caso a chave não exista, a chave será criada e pareada com o valor fornecido.<br/>
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
Visualmente, é isso que o código fará: os elementos da lista serão transpostos para um novo dicionário, 
que organizará os elementos a partir das iniciais das palavras da lista.<br/>

![image](https://github.com/user-attachments/assets/bacee93f-8080-4ed8-a2a0-7f51a9686973)


### Implementação:<br/>
* Lista "palavras": lista de palavras que serão organizadas no dicionário.<br/>
* Dicionário "por_inicial": dicionário que organizará o conteúdo a partir das iniciais dos valores.<br/>
* String "inicial": uma string de um caractere, a letra inicial da palavra.<br/>

```python
palavras = ['manga', 'alface', 'beterraba', 'melancia','abacate', 'banana'] # lista original de palavras
print(palavras) # ['manga', 'alface', 'beterraba', 'melancia', 'abacate', 'banana']
por_inicial = {} # dicionário vazio
for palavra in palavras:
    inicial = palavra[0] # letra inicial da palavra
    por_inicial.setdefault(inicial, []).append(palavra) # key = inicial, value = lista de palavras com a inicial
print(por_inicial) # {'m': ['manga', 'melancia'], 'a': ['alface', 'abacate'], 'b': ['beterraba', 'banana']}
```
