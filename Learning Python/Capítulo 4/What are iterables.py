# An object is iterable if it is either a physically stored sequence
# in memory, or an object that generates one item at a time in the
# context of an iteration operation - a sort of "virtual" sequence.
# Vale para files, ranges, maps. Os resultados são "atrasados" (deferred)
# até o momento em que algum dado se torna necessário.
# Isso economiza memória e minimiza atrasos.
# Usamos sorted(D) porque o dicionários são iterable e retornam automaticamente uma chave
# com um next para a chave seguinte.

S = "abcdef"
for c in S:
    print(c, end = " ") # a b c d e f 

print()
for n in range(2, 10):
    print(n, end = " ") # 2 3 4 5 6 7 8 9

print()
for e in [0, 3, 6, 9, 12]:
    print(e, end = " ") # 0 3 6 9 12

print()
for k in {'nome': 'paulo', 'idade': '53'}:
    print(k, end = " ") # nome idade

print()
for d in {'nome': 'paulo', 'idade': '53'}.values():
    print(d, end = " ") # paulo 53
