# Iterables não calculam a sequência inteira ao serem criados.
# Isso preserva a memória em situações em que não precisamos de todos os elementos disponíveis de imediato.
# Por isso, "range(5)" não exibe os 5 valores no print.
# Para os valores serem CALCULADOS e, então poderem ser exibidos, precisamos converter o range em uma lista.
# Ou utilizar o range numa list comprehension.

quadrados = []
print(quadrados) # []

print([x**2 for x in range(10)]) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

quadrados = [x**2 for x in range(10)]
print(quadrados) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(range(5)) # range(0, 5) Nenhum elemento está sendo calculado: nada a apresentar.
print([range(5)]) # [range(0, 5)] # idem. 
print([a for a in range(5)]) # [0, 1, 2, 3, 4] Cálculo de cada um dos 5 elementos da lista.
print(range(5)[3]) # 3 Cálculo do quarto elemento da lista.
print(list(range(5))) # [0, 1, 2, 3, 4] Para criar a lista, é preciso calcular os 5 elementos do iterável.
print(range(1000000)[10000]) # 10000 Cálculo do elemento da posição 10.000. Nenhum dos 999.999 elementos está na memória.
