# Revisão de Python no capítulo 2
# anotei as novidades para mim.

# pequeno estudo sobre a criação de uma função.
def add_numbers(a,b):
    """
    Adiciona dois números.

    Retorna
    -------
    a soma: tipo do argumento mais "extenso".
    """
    return a + b

# É possível separar múltiplos comandos numa mesma linha usando ponto e vírgula.
# E é possível utilizar ; no fim de linhas, como em C.
print(add_numbers(2, 3))
a=5; b=10; c=10  # noqa: E702
print(a,b,c)
a=6;  # noqa: E703
b=11
c=20
print(a,b,c)

# funções têm classe também. 
print(type(add_numbers)) # <class 'function'>

# a e b são referências à mesma lista (pois b = a). Como listas são mutáveis, alterar b produz a mesma alteração em a.
a = [1,2,3]
b = a
print(a, b) # [1, 2, 3] [1, 2, 3]
print('a e b referem-se ao mesmo objeto:', a is b) # True
b.append(4)
print(a,b) # [1, 2, 3, 4] [1, 2, 3, 4]
print('a e b referem-se ao mesmo objeto:', a is b) # True

# porém, como strings são imutáveis, ao alterar b, estamos criando uma nova string (uma nova referência).
print()
a = 'abc'
b = a
print(a,b)
print('a e b referem-se ao mesmo objeto:', a is b) # True
print(a,b) # abc abc
b = 'abcd'
print(a,b) # abc abcd
print('a e b referem-se ao mesmo objeto:', a is b) # False

# strings de múltiplas linhas: utilize aspas triplas ''' ou """
c = '''
strings de múltiplas linhas
são suportadas em Python.'''
print(c)
d = """
strings de múltiplas linhas
são suportadas em Python."""
print(d)

# contagem da quantidade de uma subsequência na string
print(c.count('\n'))

# \ é o escape character
print('abc\\d') # abc\d

# formatação de strings utilizando templates:
print()
template1 = '{0:.2f} {1:s} equivalem a {2:d} dólares.'
print(template1) # {0:.2f} {1:s} equivalem a {2:d} dólares.
print(template1.format(1, "Real Brasileiro", 6)) # 1.00 Real Brasileiro equivalem a 6 dólares.

from datetime import datetime, date, time  # noqa: E402, F401
dt = datetime(2025, 1, 1, 13, 54, 10)
print('Dia', dt.day, 'Minuto', dt.minute) # Dia 1 Minuto 54
print(dt.date()) # 2025-01-01
print(dt.time()) # 13:54:10
print(dt.strftime('%d-%m-%y %H:%M')) # 01-01-25 13:54

# break interrompe o for atual e retorna para o anterior.
# 0 0
# 1 0
# 1 1
# 2 0
# 2 1
# 2 2
# 3 0
# 3 1
# 3 2
# 3 3
for i in range(4):
    for j in range(4):
        if j > i:
            break
        print(i,j)

# soma dos números múltiplos de 3 ou múltiplos de 5 entre 0 e 99999:
total = 0
for i in range(100_000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
