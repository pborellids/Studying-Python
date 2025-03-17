# os números aparecem em vários tipos em Python:
# integer, ponto flutuante, complexos, decimais (precisão fixa),
# frações, sets, booleanos, funções e módulos (round, math, random etc.)
# expressões, inteiros de precisão ilimitada, operações bitwise, formatos hex, oct, bin
# extensões de terceiros: vectors, libraries, visualization, plotting etc.

# bases numéricas: decimal, hexadecimal, octal, binário.
# Usamos "0" + símbolo x, o, b:
    # 0x ou 0x = hexadecimal
    # 0o ou 0O = octal
    # 0b ou 0B = binário

from decimal import Decimal # do módulo "decimal" importe apenas a função "Decimal"
# import decimal # do módulo "decimal", importe tudo.

print()
print('Números nos 4 formatos principais (decimais, hexadecimais, octais e binários:')
print('- decimal 100 = decimal', 100) # decimal 100 = decimal 100
print('- hexadecimal 100 = decimal', 0x100) # hexadecimal 100 = decimal 256
print('- octal 100 = decimal', 0o100) # octal 100 = decimal 64
print('- binário 100 = decimal', 0b100) # binário 100 = decimal 4

# Para converter números entre a base decimal e as outras, usamos as funções hex, oct e bin.
# essas funções representam os números como strings.
# convertendo o decimal 17 para as outras 3 bases:
print()
print(hex(17)) # 0x11 (string)
print(oct(17)) # 0o21 (string)
print(bin(17)) # 0b10001 (string)

# É possível até utilizar bases arbitrárias! A função int aceita uma base arbitrária como parâmetro.
print()
print(int('14', 5)) # 14 na base 5 = 5 + 4 = 9
print(int('14', 16)) # 14 na base 16 = 16 + 4 = 20
print(int('123',0)) # Como 123 já está na forma decimal, o resultado será 123.
print(int('0xFF', 0)) # Como 0xFF já está na forma hexadecimal, o resultado será 255

# números complexos: usamos "j". Quando a parte imaginária é 1, deve-se declarar 1j, não apenas j.
# podemos também declarar um número complexo usando a função "complex(real, imag)."
print('\nQuando a parte imaginária é 1, deve-se escrever 1j:')
print(3+1j) # (3+1j) (números complexos são impressos entre parêntesis no Python)
print(1j) # 1j
print(complex(8,-3)) # (8-3j)

# para testar se um número é complexo:
print('\nPara testar se um número é complexo, usamos "isinstance(x,complex)":')
numbers = [2, 3+5j] # lista com dois números, um real e um complexo. Vamos testar cada um.
tipo = 'real'
for x in numbers:
    if isinstance(x,complex): # testando se o número é complexo
        tipo = 'complexo'
    print(x, 'é', tipo) # 2 é real
                        # (3+5j) é complexo

# Números escritos com expoente são convertidos em floating.
print(5.1e3) # 5100.0 ponto flutuante porque o original está com expoente.
print(5.1E3) # 5100.0 ponto flutuante porque o original está com expoente.
print(5100) # 5100 inteiro, porque o original está inteiro.
print(5100.0) # 5100.0 ponto flutuante porque o original já está em flutuante.
print(5e3) # 5100.0 porque o original está com expoente.
print(5e-3) # 0.005 porque o original está com expoente, se bem que aqui daria flutuante ce qualuer jeito.

# Números podem ter "type-specific" methods.
# Floats têm o método "is_integer" para indicar se correspondem a um inteiro.
# Obs: Um inteiro não terá esse método. 
print()
print('5.0 é inteiro?', 5.0.is_integer()) # True
print('5.6 é inteiro?', 5.6.is_integer()) # False
# print(5.is_integer()) # dará erro de sintaxe (SyntaxError: invalid syntax. Perhaps you forgot a comma?).

# Floats têm o método _as_integer_ratio, para convertê-los em fração.
print()
print(1.5.as_integer_ratio()) # (3, 2)
print(15.0.as_integer_ratio()) # (15, 1)
print(1.1.as_integer_ratio()) # (2476979795053773, 2251799813685248) ao invés de (11, 10)
# Alguns decimais não são exatos em Python, pois ele os converte por default em floats.
# Precisamos garantir que nosso decimal será tratado realmente como decimal pelo Python.
# A função "Decimal" (do módulo "decimal") nos ajudará. O argumento da função será a string '1.1'.
# Assim, a função converterá a string '1.1' para o decimal exato 1.1, eliminando o problema da representação em float.
print('o float 1.1 é, na verdade, ', Decimal(1.1)) # 1.1 é 1.100000000000000088817841970012523233890533447265625
print('a string "1.1" pode ser convertida no decimal 1.1:', Decimal('1.1')) # Agora temos 1.1.
print(Decimal('1.1').as_integer_ratio()) # (11, 10) Podemos agora calcular a fração reduzida.

# o método bit_length, específico do tipo integer, fornece o número de bits usados para representar o integer.
# Mas não consegui aplicar o método diretamente no número. Precisei atribuir o número a uma variável antes.
print()
x = 15
y = 16
print('Quantidade de bits para representar dec', x, '=', x.bit_length(), end = "") 
print(', pois 15 = binário', bin(15), end = ".\n") # Quantidade de bits para representar dec 15 = 4, pois 15 = 0b1111.
print('Quantidade de bits para representar dec', y, '=', y.bit_length(), end = "") 
print(', pois 16 = binário', bin(16)) # Quantidade de bits para representar dec 16 = 5, pois 16 = 0b10000

# Operadores numéricos
print()
x = 20
y = 3.3
print('x =', x, ', y = ', y)
print('soma:', x + y) # soma
print('diferença:', x - y) # diferença
print('produto:', x * y) # produto
print('quociente:', x / y) # quociente
print('parte inteira do quociente:', int(x // y), ', resto do quociente:', x % y)

# deslocamentos de bits (à esquerda, multiplica por 2; à direita, divide por 2)
print('\nDeslocar bits à esquerda = multiplicar por 2; à direita, = dividir por 2.')
print('20 =', bin(x) + ', 20 << 1 =', bin(20 << 1), '=', 20 << 1, "(1 bit à esquerda)") # 20 = 0b10100, 20 << 1 = 0b101000 = 40
print('20 =', bin(x) + ', 20 >> 1 =', bin(20 >> 1), '=', 20 >> 1, "(1 bit à direita)") # 20 = 0b10100, 20 >> 1 = 0b1010 = 10

# OR e AND: "|"" e "&"
x = 20
y = 7
print('x =', x, '=', bin(x)) # x = 20 = 0b10100
print('y =', y, '=', bin(y)) # y =  7 = 0b00111 (zeros adicionados para facilitar comparação)
print('x | y =', x | y, '=', bin(x | y)) # x | y = 23 = 0b10111
print('x & y =', x & y, '=', bin(x & y)) # x & y =  4 = 0b00100 (zeros adicionados)

