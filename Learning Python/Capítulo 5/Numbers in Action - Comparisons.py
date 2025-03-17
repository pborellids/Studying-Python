from math import pi, e, sqrt

# Normal Comparisons
# a comparação de igualdade é feita com o sinal duplo "=="
# se houver mais de um tipo numérico, o tipo menor será convertido para o tipo maior.
print('1 < 2:', 1 < 2) # True
print('2 = 2:', 2 == 2) # True
print('2 < -5:', 2 < -5) # False
print('-8 <= -8:', -8 <= -8) # True
print('pi != e:', pi != e) # True
print('2 == 2.00:', 2 == 2.00) # True

# Chained Comparisons
print()
print('1 < 4 < 10 < -50:', 1 < 4 < 10 < -50) # False
print('sqrt(5) < pi < 10.1 <= 100:', sqrt(5) < pi < 10.1 <= 100) # True

# comparações entre floats podem ser problemáticas.
print('1.1 + 2.2 == 3.3:', 1.1 + 2.2 == 3.3) # False. Porque 1.1 + 2.2 = 3.3000000000000003
print('Pois 1.1 + 2.2 =', 1.1 + 2.2) # 3.3000000000000003
print('Aproximando o resultado para uma casa decimal: 1.1 + 2.2 == %.1f' % (1.1 + 2.2)) # 1.1 + 2.2 == 3.3
# COMO TESTAR A EXPRESSÃO ACIMA: 1.1 + 2.2 == 3.3 (???) Consegui calcular com as casas decimais corretas (aproximando para uma casa).
# mas como avaliar o valor lógico da expressão, agora que está correta?

