# A função zip()
## O que a função faz
Basicamente, a função zip produz um iterável de n tuplas a partir de outros iteráveis utilizados como argumentos da função.
O número de elementos das tuplas corresponde à quantidade de argumentos usados ao chamar a função.

## Exemplo
Suponha que tenhamos estas listas:<br/>
```python
lista1 = ['Bianca', 'Pedro', 'Márcia', 'Joel'] # lista de 4 nomes de alunos
lista2 = [6,8.5,10,8] # lista de 4 notas de provas desses alunos
```
<br/>

O comando ```zip(lista1,lista2)``` produzirá, na memória do programa, este conjunto de tuplas:<br/>
|ID da Tupla|Tupla|
|:---:|:---:|
|1|('Bianca', 6)|
|2|('Pedro', 8.5)|
|3|('Márcia', 10)|
|4|('Joel', 8)]|


Podemos consultar a posição da memória em que estão as tuplas:<br/>
```print(zip(lista1,lista2))```
<br/>
O resultado seria algo neste formato: <zip object at 0x000002058760DDC0>, a posição de memória onde as tuplas iniciam. Não é muito útil, né?<br/><br/>

A função fica útil quando produzimos algum iterável (lista, conjunto, dicionário, tupla) a partir do iterável zip:<br/>
```python
lista_consolidada = list(zip(lista1,lista2))
```
[('Bianca', 6), ('Pedro', 8.5), ('Márcia', 10), ('Joel', 8)]<br/><br/>

```python
conjunto_consolidado = set(zip(lista1,lista2))
```
{('Pedro', 8.5), ('Bianca', 6), ('Joel', 8), ('Márcia', 10)} (a ordem dos elementos do conjunto **<ins>pode mudar</ins>**)<br/><br/>

```python
dicionario_consolidado = dict(zip(lista1,lista2))
```
{'Bianca': 6, 'Pedro': 8.5, 'Márcia': 10, 'Joel': 8}<br/><br/>

##Consolidando duas listas em um único dicionário<br/>
```python
for chave,valor in zip(lista1,lista2):
    dic1[chave] = valor
print(dic1)
```
{'Bianca': 6, 'Pedro': 8.5, 'Márcia': 10, 'Joel': 8}<br/><br/>

## Observação importante<br/>
Como iteráveis em geral, o iterável será perdido após o primeiro uso (iterável é exaurido após ser percorrido).<br/>
Isso é uma providência inteligente da linguagem Python, a fim de evitar o consumo de recursos desnecessários.<br/><br/>
Primeiro uso do iterável:<br/>
```python
zipped = zip(lista1,lista2)
print(list(zipped))
```
[('Bianca', 6), ('Pedro', 8.5), ('Márcia', 10), ('Joel', 8)]<br/><br/>
Segundo uso do iterável:<br/>
```python
print(list(zipped))
# Não há conteúdo agora.
```
[]
