S1="Biologia Molecular da Célula"
S1=S1.split(' ',5)
print(S1) # ['Biologia', 'Molecular', 'da', 'Célula']

# for loops
for c in "livro":
    print(c.upper(), end = "/") # L/I/V/R/O/

# while loops
print()
x = 5
while x > 0:
    print('Livro' * x)
    x -= 1
# LivroLivroLivroLivroLivro
# LivroLivroLivroLivro
# LivroLivroLivro
# LivroLivro
# Livro
