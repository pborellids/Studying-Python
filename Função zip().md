# A função zip()
## O que a função faz
Basicamente, a função zip produz um iterável de n tuplas a partir de outros iteráveis utilizados como argumentos da função.
O número de elementos das tuplas corresponde à quantidade de argumentos usados ao chamar a função.

##Exemplo
Suponha que tenhamos estas listas:
lista1 = ['Bianca', 'Pedro', 'Márcia', 'Joel'] # lista de 4 nomes de alunos
lista2 = [6,8.5,10,8] # lista de 4 notas de provas desses alunos

O comando zip(lista1,lista2) produzirá, na memória do programa, este conjunto de tuplas:<br/>
Número da Tupla  |     Tupla<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1        |  ('Bianca', 6)<br/>
`` `` `` 2        |  ('Pedro', 8.5)<br/>
3        |  ('Márcia', 10)<br/>
4        |  ('Joel', 8)]<br/>
Podemos consultar a posição da memória em que estão as tuplas:
print(zip(lista1,lista2))
O resultado seria algo neste formato: <zip object at 0x000002058760DDC0>, a posição de memória onde as tuplas iniciam. Não é muito útil, né?

A função fica útil quando produzimos algum interável (lista, conjunto, dicionário, tupla) a partir do iterável zip:
lista_consolidada = zip(lista1,lista2):
[('Bianca', 6), ('Pedro', 8.5), ('Márcia', 10), ('Joel', 8)]

conjunto_consolidado = zip(lista1,lista2)
{('Pedro', 8.5), ('Bianca', 6), ('Joel', 8), ('Márcia', 10)} (a ordem dos elementos do conjunto pode mudar)

dicionario_consolidado = zip(lista1,lista2)
{'Bianca':6, 'Pedro':8.5, 'Márcia':10, 'Joel':8}

##Consolidando duas listas em um único dicionário
for chave,valor in zip(lista1,lista2):
    dic1[chave] = valor
print(dic1)
{'Bianca':6, 'Pedro':8.5, 'Márcia':10, 'Joel':8}

## Observação importante
Como iteráveis em geral, o iterável será perdido após o primeiro uso (iterável é exaurido após ser percorrido).
zipped = zip(lista1,lista2)
Primeiro uso do iterável:
print(list(zipped))
[('Bianca', 6), ('Pedro', 8.5), ('Márcia', 10), ('Joel', 8)]
Segundo uso do iterável:
print(list(zipped))
[]
Não há conteúdo agora.
