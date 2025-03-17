print(0o1, 0o20, 0o377) #1 16 255
print(0x01, 0x10, 0xFF) #1 16 255
print(0b1, 0b10000, 0b11111111) #1 16 255
print(oct(64), hex(64), bin(64)) # 0o100 0x40 0b1000000
print(int('64'), int('100',8), int('40', 16), int('1000000', 2))
print(int('0x40', 16)) # 64

# eval é uma função interessante. Ela trata strings como códigos Python.
eval('print(1+1)') # 2
# a função eval compilará o argumento (a string 'print(1+1)', que tem como resultado o valor 2.

# a função eval compilará o argumento (primeiro 'print'). 
# O 1o print tem a string "print(1+1)" como argumento. 
# Por isso, o eval executará o 1o print, que imprimirá o 2o print e seu próprio argumento.
eval('print("print(1+1)")') # print(1+1)

# conversão de inteiros para bases diversas
print('%o, %x, %x, %X' % (64, 64, 255, 255))
print(int('64',16))

# as funções "int", "bin", "oct" e "hex" retornam strings.
print(bin(1))
print(bin(10))
print(oct(10))
print(hex(70))

# o método "bit_length" calcula o número de bits para representar o número consultado.
x = 34
print(x.bit_length()) # 6 bits para representar o 34 em binário.

# as funções pow e abs são built-in.
print(pow(2,4)) # 2 ** 4 = 16
print(abs(3+4j)) # 5.0 Módulo do número

# sum soma todos os elemntos do iterable.
print(sum((1,2,3,4,4,1,3))) # 18 (soma do elementos da tupla)
print(sum([1,2,3,4,4,1,3])) # 18 (soma dos elementos da lista)
print(sum({1,2,3,4,4,1,3})) # 10 (soma dos elementos do conjunto, sem contar as repetições)

# mínimo e máximo do iterable. Num dict, o mínmo ou máximo se refere às strings das chaves, não aos valores.
print(min(1,2,3,4,4,3,1,1000,-5))
print(max(1,2,3,4,4,3,1,1000,-5))
print(min([1,2,3,4,4,3,1,1000,-5]))
print(min({'b': 1, 'c':2, 'a': 3, 'd': 4, 'e': 4, 'f':3, 'g': 1, 'i': 1000, 'h': -5})) # "a" - mínimo entre as chaves.
print(max({'b': 1, 'c':2, 'a': 3, 'd': 4, 'e': 4, 'f':3, 'g': 1, 'i': 1000, 'h': -5})) # "i" - máximo entre as chaves.

import random  # noqa: E402
print(random.random())
print(random.randint(0,10))
print(random.choice(['Matemática Financeira', 'Palestine', 'Álgebra Linear', 'Introduction to Algorithms'])) # escolhe um elemento.
lista = ['The Data Science Handbook', 'Nexus', 'O Xangô de Baker Street', 'Uma História (muito) curta da vida na Terra']
random.shuffle(lista) # retorna none, mas embaralha a lista diretamente.
print(lista)

print()
print(0.1 + 0.1 + 0.1 - 0.3)
import decimal # função Decimal retorna um número decimal preciso a partir da string.  # noqa: E402
print(decimal.Decimal('0.1')) # 0.1 na forma de um número decimal preciso.
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')) # resultado decimal preciso.

print()
# a função Decimal também aceita números como argumento. Entretanto, poderá ter problemas de falta de bits para representá-los.
print(decimal.Decimal(0.1)) # 0.1000000000000000055511151231257827021181583404541015625

# Definir a precisão do Decimal é possível (método getcontext).
print(decimal.Decimal(1) / decimal.Decimal(7)) # 0.1428571428571428571428571429
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7)) # 0.1429

