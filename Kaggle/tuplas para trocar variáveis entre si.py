# é possível trocar variáveis entre si com muita facilidade utilizando tuplas.
a = 4
b = 5
c = 6
d = (6, 7)
tup = a, b, c, d
print(a, b, c, d)
a, b, c, d = b, d, c, a
print(a, b, c, d) # 5 (6, 7) 6 4
a, b, c, d = c, a, d, b
print(a, b, c, d) # 6 5 4 (6, 7)
