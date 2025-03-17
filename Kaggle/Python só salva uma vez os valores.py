# str1 tem o valor 'abc'. Python associa o valor 'abc' à posição de memória em que ele está. 
# Sempre que o valor 'abc' voltar a ser utilizado, Python usará não o valor, mas a referência a ele.
str1 = 'abc'
print(id(str1), id('abc')) # str1 e 'abc' indicam a mesma posição de memória.

# Na tupla, o segundo valor é 'cde'. A tupla aponta somente para as referências.
# Se o valor 'cde' é utilizado fora da tupla, a referência segue sendo a que a tupla utiliza no segundo elemento dela.
T = ('ab', 'cde', 'ac')
print("'", T[1], "' como segundo elemento da tupla: ", id(T[1]), sep = '') # 'cde' como segundo elemento da tupla: 2394835696736
print("'cde'", id('cde')) # 'cde' 2394835696736
