# A função zip()
## O que a função faz
Basicamente, a função zip produz um iterável de n tuplas a partir de outros iteráveis utilizados como argumentos da função.
O número de elementos das tuplas corresponde à quantidade de argumentos usados ao chamar a função.

##Exemplo
Suponha que tenhamos estas listas:
lista1 = ['Bianca', 'Pedro', 'Márcia', 'Joel'] # lista de 4 nomes de alunos
lista2 = [6,8.5,10,8] # lista de 4 notas de provas desses alunos

O comando zip(lista1,lista2) produzirá, na memória do programa, este conjunto de tuplas:<br/>
Número&nbsp;&nbsp;|<br/>
&nbsp;&nbsp;&nbsp;da&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tupla<br/>
&nbsp;Tupla&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;('Bianca', 6)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;('Pedro', 8.5)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;('Márcia', 10)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;('Joel', 8)]<br/>
Podemos consultar a posição da memória em que estão as tuplas:<br/>
print(zip(lista1,lista2))<br/>
O resultado seria algo neste formato: <zip object at 0x000002058760DDC0>, a posição de memória onde as tuplas iniciam. Não é muito útil, né?<br/><br/>

A função fica útil quando produzimos algum iterável (lista, conjunto, dicionário, tupla) a partir do iterável zip:<br/>
lista_consolidada = zip(lista1,lista2):<br/>
[('Bianca', 6), ('Pedro', 8.5), ('Márcia', 10), ('Joel', 8)]<br/><br/>

conjunto_consolidado = zip(lista1,lista2)<br/>
{('Pedro', 8.5), ('Bianca', 6), ('Joel', 8), ('Márcia', 10)} (a ordem dos elementos do conjunto pode mudar)<br/><br/>

dicionario_consolidado = zip(lista1,lista2)<br/>
{'Bianca':6, 'Pedro':8.5, 'Márcia':10, 'Joel':8}<br/><br/>

##Consolidando duas listas em um único dicionário<br/>
for chave,valor in zip(lista1,lista2):<br/>
    dic1[chave] = valor<br/>
print(dic1)<br/>
{'Bianca':6, 'Pedro':8.5, 'Márcia':10, 'Joel':8}<br/><br/>

## Observação importante<br/>
Como iteráveis em geral, o iterável será perdido após o primeiro uso (iterável é exaurido após ser percorrido).<br/>
Isso é uma providência inteligente da linguagem Python, a fim de evitar o consumo de recursos desnecessários.<br/>
zipped = zip(lista1,lista2)<br/>
Primeiro uso do iterável:<br/>
print(list(zipped))<br/>
[('Bianca', 6), ('Pedro', 8.5), ('Márcia', 10), ('Joel', 8)]<br/>
Segundo uso do iterável:<br/>
print(list(zipped))<br/>
[]<br/>
Não há conteúdo agora.<br/>
