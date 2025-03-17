# Um função é criada através do stetement "def". 
# O identificador "soma" é atribuído às operações que estão na parte identada.
def soma(num1, num2):
    return num1 + num2

# para chamar uma função, basta utilizar o nome do objeto:
print('soma(1, -4) =', soma(1,-4))

# funções podem ser atribuídas a outros objetos:
nova_soma = soma
print('nova_soma (1, -5) =', nova_soma(1,-5))

# funções podem ser atribuídas a variáveis:
x = soma(2,-10)
print('x =', x)

# até mesmo funções "built-in" podem ser atribuídas a novos objetos, que podem ser utilizados normalmente em lugar da função original.
newlen = len # aqui, a função built-in "len" é atribuída a um novo objeto.
print('newlen(\'abc\') =', newlen('abc'))

# funções são "typeless":
print(soma('abc','cde'))
print()

# INTERSECÇÃO ENTRE DUAS SEQUÊNCIAS
# OPÇÃO 1 - LISTA
# função que devolve a intersecção entre duas sequências (com iterações aninhadas = lento).
# Há um defeito: se um caracter estiver repetido na primeira sequência, ele aparecerá duas vezes no resultado
# (que deveria funcionar como uma intersecção).
def intersect(s1, s2):
    res = []
    for x in s1: # se o caracter x estiver repetido, o loop será executado repetidas vezes, e o resultado terá duplicações.
        if x in s2:
            res.append(x) # retorna uma lista.
    s1 = '' # variável local. Essa alteração não terá efeito fora da função.
    s2 = '' # variável local. Essa alteração não terá efeito fora da função.
    print('id(s1) na função \"intersect\":', id(s1)) # a variável da função tem referência diferente da variável usada na chamada.
    return res
# OPÇÃO 2 - SET
# função que devolve a intersecção entre duas sequências (com set).
# Aqui, evita-se a repetição de caracteres, porque é utilizado o operador intersecção.
def intersect2(seq1,seq2):
    res = set(seq1) & set(seq2)
    return res # retorna um conjunto.

# s1 = 'a3bacd' # s1 leva ao problema da duplicação de letras no resultado de duas das três opções de intersecção.
s1 = 'a3bcd'
s2 = 'ade3'
print('id(s1) no programa principal:', id(s1))
print('\nLista:             ', intersect(s1, s2))
print('Set:               ', intersect2(s1, s2))

# OPÇÃO 3 - LIST COMPREHENSION
# A list comprehension evita a necessidade de uma função separada, pois podemos usar uma única linha.
# porém, mantém o problema da repetição do caracter se a 1a sequência tiver repetição.
intersect3 = [x for x in s1 if x in s2] # bem curta, mais eficiente, mas mantém o problema da duplicação de letras no resultado.
print('List Comprehension:', intersect3)


# Imutabilidade x Referência
print('Mistura de tipos (string e tupla):', intersect2(s1, ('a', 'd', 'e', '3')))

print('s1 e s2 foram esvaziadas na primeira função. Mas seus valores permanecem preservados fora da função:')
print('s1 = ', s1, ', ', 's2 = ', s2, sep = '')

# IMUTABILIDADE DO TIPO INTEIRO
# Python associa posições pré-definidas de memória a cada inteiro que é declarado no programa.
# Aqui, a posição 140721290085288 se torna permanentemente associada ao valor 1.
# Quando "b" é declarado sendo igual a "a", "b" passa a apontar para a mesma posição já apontada por "a".
a = 1 # O valor 1 é escrito na posição de memória 140721290085288. "a" é ponteiro para 1 (140721290085288).
b = a # "b" também é um ponteiro para 1 (140721290085288).
print('\n*** IMUTABILIDADE DO TIPO INTEIRO ***')
print('a = ', a, ', b = ', b, sep = '', end = '')
print(', \'a\' e \'b\' apontam para a mesma posição de memória:')
print('id(a) =', id(a), '= posição do valor 1.') # 140721290085288
print('id(b) =', id(b), '= posição do valor 1.') # 140721290085288
# Python associa cada inteiro a uma posição pré-definida, exclusiva e imutável.
# O endereço 140721290085480 é associado ao valor 7. "a" aponta para essa nova posição (140721290085480).
a = 7 # endereço 140721290085480
# b continua apontando para a posição 140721290085288, onde está o valor 1.
# O endereço onde está armazenado o inteiro 1 é "IMUTÁVEL". A nova declaração "a = 7" associa um endereço novo ao valor "7",
# e "a" passa a apontar para esse novo endereço.
print()
print('a =', a, 'b = ', b)
print('id(a) =', id(a)) # 140721290085480
print('id(b) =', id(b)) # 140721290085288

# Curiosidade: Python associa o valor 1 à posição 140721290085288. 
# Novas variáveis que venham a ser associadas ao valor 1, também apontarão para essa mesma posição.
# O valor 1 ocupa uma posição de memória própria, que não muda. Novas variáveis associadas ao valor 1 apontarão para a mesma posição.
b = 1 # b é um ponteiro para 1 (140721290085288).
c = 1 # b é um ponteiro para 1 (140721290085288).
print()
print('b = ', b, ', c = ', c, sep = '', end = '')
print(', \'b\' e \'c\' apontam para a mesma posição de memória:')
print('id(b) =', id(b)) # 140721290085288
print('id(c) =', id(c)) # 140721290085288
print('Que é exatamente a posição ocupada pelo inteiro 1:')
print('id(1) =', id(1)) # 140721290085288
