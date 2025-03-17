# básico de strings:
# - criar duas strings, S1 e S2
# - contabilizar o comprimento de cada uma
# - acessar um caractere específico de cada
#   - índice da posição do caractere: contado como deslocamento a partir 
#     do início da string
#       - por isso, o índice começa em 0
#       - por isso, para ler o último caractere, podemos usar índice = "-1"
#       - Exemplos:
#           - S[0] = primeiro caractere da string
#           - S[2] = terceiro caractere da string 
#           - S[-1] = último caractere da string
#             (deslocamento "-1" a partir do fim)
#           - S[-3] = antepenúltimo caractere da string
#             (deslocamento "-3" a partir do fim)
# - obter uma "fatia" (slice)
#   - fatias são subsequências contínuas da string
#     - definimos o deslocamento do 1o caractere e
#       definimos o deslocamento do primeiro caractere a ignorar

# ------- TESTES DE ÍNDICES -------
print("\n")
print("------- TESTES DE ÍNDICES -------","\n"*2)
S1 = 'Ventilador'
S2 = "Ar Condicionado"
print("Comprimento de S1:", len(S1))
print("Comprimento de S2:", len(S2))
# o comando "print" utiliza como separador default o caractere de espaço.
# por isso, ao utilizar duas ou mais strings, o comando automaticamente as separa por espaços.
# já na concatenação, não há espaços entre as strings.
print("S1[0]:" + S1[0]) #concatenação: print não insere espaço entre as strings.
print("S1, S2, (sep default):", S1, S2) #imprimir duas strings insere um espaço entre elas automaticamente
print("S1, S2, (sep ','): ", end = "") # end = "" evita que o print termine com new line
print(S1, S2, sep = ", ")
print("S2[0]:",S2[0])
print("S1[1]:",S1[1])
print("S2[-2]",S2[-2])
print("S1[len(S1)-3]",S1[len(S1)-3])
print("S1[9]", S1[9],"\n")

# ------- SLICES -------

print("------- TESTE DE SLICES -------","\n"*2)
# slices EXCLUEM a posição do segundo elemento
# slice de 2:5 terá 3 elementos, não 4.
print("Slice com 3 elementos: S[2] até S[4] inclusive:",S1[2:5]) # (="nti")
print("substring com 4 elementos: S[2] até S[5] inclusive:",S1[2]+S1[3]+S1[4]+S1[5]+"\n") # (="ntil")

# "tilador": ignora o caractere S[10], que não existe.
print("S1[3:len(S1)] Slice 'tilador'?","Resposta:",S1[3:len(S1)],"\n")
# "Condicionad": ignora o último caractere (caractere S[9]).
print("S2[3:-1] Slice 'Condicionad'?","Resposta:",S2[3:-1],"\n")
# "tilador": ignora o caractere S[10], que não existe.
print("S1[3:10] Slice 'tilador'?","Resposta:",S1[3:10],"\n")
# "Condicionad": ignora o último caractere (caractere S[9]).
print("S2[3:14] Slice 'Condicionad'?","Resposta:",S2[3:14],"\n")

# defaults: deslocamento inicial = 0; deslocamento final = len(str)
print("S1[:]",S1[:])
print("S1[0:]",S1[0:])
print("S1[:len(S1)]",S1[:len(S1)]) # ir até imediatamente antes do 11o.
print(S1[:10]) #ir até imediatamente antes do 11o.
print(S1[:20]) #ir até imediatamente antes do 21o.

# Polimorfismo do + ocorre entre objetos do mesmo tipo
# não entre misturas de tipos
print("1+2"+"abc") # OK (concatena as duas strings)
print(1+2) # OK (soma os dois números)
# print(1+2+"abc") # NOK
