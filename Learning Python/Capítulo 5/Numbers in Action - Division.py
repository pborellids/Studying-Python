import math
# x / y: true division, mantém o resto em forma float
print('2 / 3 =', 2 / 3) #  0.6666666666666666
print('3 / 2 =', 3 / 2) # 1.5
print('6 / 2 =', 6 / 2) # 3.0

# x // y: floor division. Trunca para o inteiro inferior.
# Atenção: a floor division NÃO trunca o número para o inteiro. Ela arredonda para o inteiro inferior.
print()
print('2 // 3 =', 2 // 3) # 0
print('20 // 3 =', 20 // 3) # 6
print('20 // 3.0 =', 20 // 3.0) # 6.0
print('20.0 // 3 =', 20.0 // 3) # 6.0
print('20.0 // 3.0 =', 20.0 // 3.0) # 6.0

# x // y, floor division, opera um arredondamento para o inteiro inferior. Com números negativos:
print()
print('Floor division de -20 // 6 =', -20 // 6) # -4
print('Floor division de 20 // 6 =', 20 // 6) # 3

# mais sobre floor e trunc:
print()
print('floor(2.5) = ', math.floor(2.5)) # 2
print('floor(-2.5) = ', math.floor(-2.5)) # -3
print('trunc(2.5) = ', math.trunc(2.5)) # 2
print('trunc(-2.5) = ', math.trunc(-2.5)) # -2

