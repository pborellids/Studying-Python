# arquivos podem ser abertos em modo leitura, escrita ou criação.
# Se não especificado, o diretório escolhido será o atual.

# Escrevendo num arquivo já existente. Método "append" (acrescenta o texto ao fim do arquivo).
# Outras opções: 'x' cria um novo arquivo; 'w' abre para escrita (sobrescrição); 'r' abre para leitura (default).

# 'utf8' é necessário na abertura do arquivo para leitura ou gravação a fim de preservar os caracteres latinos.
# utf8 é uma condificação de comprimento variável (1 a 4 bytes) e, por isso, capaz de representar milhões de símbolos.
# Python 3.15 provavelmente terá UTF8 como default abertura de arquivo texto.
# https://en.wikipedia.org/wiki/UTF-8

f = open('dados.txt', 'w', encoding = 'utf8')
f.write("Olá Mundo!\n")
f.write('criado em Python 14/12/2024\n')
f.close

# Lendo o arquivo.
f = open('dados.txt', encoding = 'utf8')
text = f.read()
print("Conteúdo:\n", text, sep = "")
print("Caracteres:", len(text), "\n")
print(text.split())
f.close

# Outro jeito de ler o arquivo (usando um iterável). Cada linha do arquivo é um item no iterável retornado pelo open.
i = 1
for line in open('dados.txt', encoding = 'utf8'):
    print(i, line, end="") # como o arquivo original foi gravado com "\n", acabaria aparecendo uma linha adicional aqui.
    i += 1
print("Type:", type(f))
f.close
