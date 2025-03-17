# Methods
# .find localiza o offset de uma string em outra string.
# .split produz uma lista usando uma string como separador.
# .join produz uma string concatenando os elementos da lista com a string na qual o método é aplicado.
# .replace substitui as ocorrências de uma string por outra string.
# LEMBRANDO: STRINGS SÃO UNMMUTABLE!

S = "Palestine, Joe Sacco"
print(S.find('Joe'))
print(S.replace('Joe', 'J.'))
print(S)
print(S.split(", ")) # lista de S usando a ", " como separador (['Palestine', 'Joe Sacco'])
print(", ".join(S.split(", "))) # junta novamnente os elementos da lista de modo idêntico à string original.

# lendo uma string .csv
StrCSV = "Palestine,Álgebra Linear,Biology 2nd Ed.,Biology - A Global Approach,Biologia Molecular da Célula,Generative Deep Learning"
listacsv = StrCSV.split(",")
print(listacsv)
print(StrCSV)
print(StrCSV.upper())
print(StrCSV.lower())
print(listacsv)
print("'listacsv' tem",len(listacsv),"itens.")
print("Is '", listacsv[0], "' alpha? ", listacsv[0].isalpha(), sep = "")
print("Is '", listacsv[1], "' alpha? ", listacsv[1].isalpha(), sep = "")
NoSpace = "".join(listacsv[1].split(" "))
print("Is '", NoSpace, "' alpha? ", NoSpace.isalpha(), sep = "")
print("Is '", listacsv[2], "' alpha? ", listacsv[2].isalpha(), sep = "")
NoSpace = "".join(listacsv[2].split(" "))
print("Is '", NoSpace, "' alpha? ", NoSpace.isalpha(), sep = "")
print("Is '", listacsv[3], "' alpha? ", listacsv[3].isalpha(), sep = "")
NoSpace = "".join(listacsv[3].split(" "))
print("Is '", NoSpace, "' alpha? ", NoSpace.isalpha(), sep = "")
print("Is '", listacsv[4], "' alpha? ", listacsv[4].isalpha(), sep = "")
NoSpace = "".join(listacsv[4].split(" "))
print("Is '", NoSpace, "' alpha? ", NoSpace.isalpha(), sep = "")
print("Is '", listacsv[5], "' alpha? ", listacsv[5].isalpha(), sep = "")
NoSpace = "".join(listacsv[5].split(" "))
print("Is '", NoSpace, "' alpha? ", NoSpace.isalpha(), sep = "")

# rstrip, lstrip: removem strings no fim ou no início da string.
Str1 = " Matemática Financeira   " # vamos converter para "Matemática Financeira removendo os espaços em branco."
print("\n", len(Str1)) # comprimento de Str1.
print(len(Str1.rstrip(" "))) # comrprimento de Str1 sem os 3 espaços à direita.
print(len(Str1.lstrip())) # comprimento de Str1 sem o espaço à esquerda.
print("XXX", " Matemática Financeira---", Str1, "XXX", sep = "") # 1 espaço à esquerda, 3 à direita.
print("XXX", " Matemática Financeira", Str1.rstrip(), "XXX", sep = "") # 1 espaço à esquerda.
print("XXX", "Matemática Financeira", Str1.rstrip().lstrip(), "XXX", sep = "") # nenhum espaço à esquerda ou direita.

# criando uma lista de Str1 sem os espaços à esquerda e direita,
# e uma string concatenando a lista com um espaço como separador.
print(Str1.rstrip().lstrip().split(" "), sep = "") # lista sem os espaços à esquerda e à direita.
print(" ".join(Str1.rstrip().lstrip().split(" ")))
print()
print("%s, eggs, %s" % ('parmesão', 'óleo')) # mais sobre formatação mais tarde.

# help com os métodos de um objeto - função dir (ou método dir)
print("dir(Str1:",dir(Str1))
print("\ndir(Str1:",Str1.__dir__())
print("\n")

# método __add__ concatena strings, mas não é recomendável utilizá-lo.
print("abc" + "XZ")
print("abc".__add__("XZ"))

# help para os métodos
print("\n HELP",help("abc".center(10,"#")))
print(dir(str))
print(help(str))