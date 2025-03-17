import math
# formato numérico no display - primeiros testes:
print()
num = 1 / 3.0
print(num) # 0.3333333333333333
print('%e' % num) # 3.333333e-01 Número estará na notação científica e terá 6 casas decimais (default)
print('%.3e' % num) # 3.333e-01, notação científica com 3 casas decimais na mantissa.
print('%4.2f' % num) # 0.33 Número terá 4 dígitos (incluindo o ponto decimal), sendo dois dígitos após o ponto decimal.
print('{0:4.2f}'.format(num)) # 0.33

# Formatação de strings.
# há duas formas de formatar strings:
# - a tradicional (expressões de formatação).
# - e a do Python 3.0 (método .format).
# ambas são praticamente equivalentes.

# FORMATAÇÃO COM EXPRESSÕES
# lado esquerdo do %: uma string de formatação, com um ou mais operadores %,
# cada um com uma regra de conversão.
# lado direito do %: o objeto a ser formatado (ou tupla com múltiplos objetos a formatar)
# esses objetos do lado direito serão inseridos na string de formatação da esquerda em lugar da regra de formatação.
# os typecodes principais são:
    # s: string
    # c: character (int or string)
    # d: inteiro na base decimal
    # i: integer
    # o: inteiro na base octal
    # x: inteiro na base hexadecimal
    # e: float com expoente
    # f: float na base decimal
print('O título deste livro %s é %s, e eu tenho %i unidade dele.' % ('azul', 'Álgebra Linear', 1))
# O título deste livro azul é Álgebra Linear, e eu tenho 1 unidade dele.
print('O título deste livro %s é %s, e eu tenho %c unidade dele.' % ('azul', 'Álgebra Linear', '1'))
# O título deste livro azul é Álgebra Linear, e eu tenho 1 unidade dele.
print('O título deste livro %s é %s, e eu tenho %d unidade dele.' % ('azul', 'Álgebra Linear', 1))
# O título deste livro azul é Álgebra Linear, e eu tenho 1 unidade dele.
print('O título deste livro %s é %s, e eu tenho %e unidade dele.' % ('azul', 'Álgebra Linear', 1))
# O título deste livro azul é Álgebra Linear, e eu tenho 1.000000e+00 unidade dele.
print('O título deste livro %s é %s, e eu tenho %f unidade dele.' % ('azul', 'Álgebra Linear', 1))
# O título deste livro azul é Álgebra Linear, e eu tenho 1.000000 unidade dele.

# fazendo a primeira formatação acima "na raça":
t = ('azul', 'Álgebra Linear', 1)
print('O título deste livro ', t[0], ' é ', t[1], ', e eu tenho ', t[2], ' unidade dele.', sep = "")
# fica claro que é MUITO MAIS FÁCIL utilizar a string de formatação!

print()
# %f escreve até a precisão indicada, mantendo os zeros necessários se for o caso.
# %a.bf formata para "a" dígitos no mínimo (ou espaços em branco se número for menor). O ponto decimal é contado.
# e "b" dígitos após o ponto decimal. 
# aparentemente, se o número tiver mais que "a" dígitos, eles serão todos representados.
# A notação %.b vale também para %.be (ou seja, casas decimais da mantissa definidas pelo "b").
print('4.1 com %%1.1f: %1.1f' % (4.1)) # 4.1 com %1.1f: 4.1, 4.1 tem mais que 1 dígito, então todos aparecem.
print('4.1 com %%2.1f: %2.1f' % (4.1)) # 4.1 com %2.1f: 4.1, 4.1 tem mais que 2 dígitos, então todos aparecem.
print('4.1 com %%3.1f: %3.1f' % (4.1)) # 4.1 com %3.1f: 4.1,  4.1 tem exatamente 3 dígitos, então todos aparecem.
print('4.1 com %%4.1f: %4.1f - 1 espaço em branco antes.' % (4.1)) # 4.1 com %4.1f:  4.1, com 1 espaço em branco antes.
print('4.1 com %%5.1f: %5.1f - 2 espaços em branco antes.' % (4.1)) # 4.1 com %5.1f:   4.1, com 2 espaços em branco antes.
print('4.1 com %%4.2f: %4.2f - 2 casas decimais.' % (4.1)) # 4.10 duas casas decimais.
print('4.1 com %%5.3f: %5.3f - 3 casas decimais.' % (4.1)) # 4.100 três casas decimais.
print('4.1 em notação científica e 4 casas decimais: %.4e' % (4.1)) # 4.1 em notação científica e 4 casas decimais: 4.1000e+00
print('Número de Euler (e) com 18 casas decimais: %.18f.' % math.e)
print('pi com 21 casas decimais: %.21f.' % math.pi)
