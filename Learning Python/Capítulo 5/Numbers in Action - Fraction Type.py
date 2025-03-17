# Assim como "Decimals", as frações não estão diretamente ligadas ao hardware
# e não sofrem das imprecisões do float portanto.
# consomem mais CPU, mas podem ser úteis ou convenientes em determinados cenários.
from fractions import Fraction
from decimal import Decimal
x = Fraction(1,3)
y = Fraction(4,6)
print(x) # 1/3
print(y) # 2/3 A fração vem reduzida.
print(x+y) # 1 (print) ou 1/1 janela imediata. Print imprime o inteiro correspondente.
print(x-y) # -1/3
print(x * y) # 2/9 fração reduzida

# Fraction() permite converter um decimal (string) em uma fração.
print()
print(Fraction('0.25')) # 1/4
print(Fraction('1.25')) # 5/4
print(Fraction('0.25') + Fraction('1.25')) # 3/2

# Fraction e Decimal resolvem o problema da precisão do float.
print()
print(0.1 + 0.1 + 0.1 - 0.3) # 5.551115123125783e-17
print(Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10)) # 0
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # 0.0

# o símbolo * expande o iterável em seus elementos.
print()
t = (1,3,5,7)
print('tupla:', t)
print('elementos da tupla:', *t)

# as_integer_ratio
print()
# f = 2.5.as_integer_ratio()
# print(f) # (5,2)
# print(*f) # 5 2
# z = Fraction(*f)
# print(z) # 5/2
f = 2.5 # f is float.
z = Fraction(*(f.as_integer_ratio())) # z is the fraction from the elements of tuple (5, 2), meaning 5/2
print(z) # 5/2 :-)

print()
print(Fraction.from_float(1.75)) # 7/4
print(1.75.as_integer_ratio()) # (7,4)
print(*1.75.as_integer_ratio()) # 7 4
print(Fraction(*1.75.as_integer_ratio())) # 7/4

print()
x = Fraction(1,3)
print(x)
print(x+2)
print(x+2.0)
print(x+(1/3))
print(x+(4/3))
print(x + Fraction(4,3))

# método "limit_denomitor" força o denominador a ser reduzido, facilitando a produção de frações amigáveis.
# cuidado: se o denominado máximo for inferior ao denominador da fração reduzida, o resultado perderá precisão
print()
x = Fraction(1,3)
a = x + Fraction(*(4.0/3).as_integer_ratio())
print(a) # 22517998136852479/13510798882111488
print(22517998136852479 / 13510798882111488) # 1.6666666666666665, praticamwente 5/3
print(a.limit_denominator(10))
print(Fraction(3.141592653589)) # 3537118876013327/1125899906842624
print(Fraction(3.141592653589).limit_denominator(100)) # 311/99
print(Fraction(3.141592653589).limit_denominator(10)) # 22/7
print(Fraction(2.6)) # 5854679515581645/2251799813685248
print(Fraction(2.6).limit_denominator(10)) # 13/5 (exato)
print(Fraction(2.6).limit_denominator(4)) # 8/3 (perda de precisão)
print(Fraction(2.6).limit_denominator(2)) # 5/2 (perda de precisão)
