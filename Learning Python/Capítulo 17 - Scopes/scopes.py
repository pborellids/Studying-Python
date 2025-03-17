# A LOCALIZAÇÃO DA DECLARAÇÃO DETERMINA O ALCANCE DO NOME
# O namespace associado ao objeto é o namespace no qual o objeto foi declarado.
# Um objeto declarado numa função tem visibilidade default apenas na função.
# Funções têm seu próprio namespace.

L = [1, 2, 3, 'z'] # L declarado globalmente. L terá escopo global.

def func1():
    L = [4, 5, 6, 'zz'] # L é local.
    L.append(7)
    return L
print(func1()) # [4, 5, 6, 'zz', 7]

def func2():
    L.append(7) # L é global.
    return L
print(func2()) # [1, 2, 3, 'z', 7]

# GLOBAL STATEMENT
print("GLOBAL STATEMENT")
w = 88
def func3():
    global w # 'w' é global.
    w = 99
func3()
print(w) # 99

y, z = 1, 2
def func4():
    global x # x é global, apesar de declarada apenas no def.
    x = y + z
func4()
print(x)

y, z = 1, 2
x = -1
def func5():
    # y e z são tratadas como globais, pois não foram declaradas dentro do def.
    # x = y + z é uma declaração de x def. Por isso, x seria considerada local.
    # A declaração x = y + z não teria efeito na variável x do módulo.
    # Por isso, global foi usado em declaração anterior de x no def.
    global x # declaração de 'x' como global.
    x = y + z # variável global sendo alterada.
func5()
print(x)

x = ''
def func6():
    global x
    x += '.' # x foi declarado na def, mas tem escopo global.
for i in range(3): # loop de 3 ciclos
    func6()
print(x) # "..."

# O escopo passa pelo nesting antes de chegar no escopo do módulo.
x = 99
def f1():
    x = 88
    def f2():
        print(x) # 88. x não foi declarada em f2. Então Python procura x em f1.
    f2()
f1()

# CLOSURE FUNCTION / FACTORY FUNCTION
# a função interna (fun2) é "salva" com os valores das variáveis que estão fora do escopo local, mas que foram declaradas na função interna.
# por isso, ao executar a "foto" da fun2, essas variáveis não locais ainda estarão disponíveis e a fun2 poderá ser executada em separado
# da função pai (fun1).
# 'action' corresponde à fun2, que imprime 'x' por acesso direto ao endereço de fun2. fun1 não estava em execução.
# Mas o valor de 'x' foi recuperado normalmente.
# CLOSURE FUNCTIONS podem ser também chamdas de "FACTORY FUNCTIONS" - porque permitem "fabricar" uma instância da função
# com um estado específico. Quanto fun1 retorna fun2, ela o faz incluindo o estado presente de x.
def fun1():
    x = 66
    def fun2():
        print(x)
    print('Endereço da fun2:', fun2) # 0x0000027F484D93A0
    return fun2 # Isto retorna uma "fotografia" das variáveis usadas em fun2 (ou seja, apenas 'x' neste caso) e o endereço de fun2. 
# Quando se quiser, pode-se executar fun2, com o valor de 'x' da fotografia, e rodá-la fora do aninhamento.
# Por isso, essa técnica se chama "fábrica de função" ou "encapsulamento de função".
# No caso, fun2 está em 0x0000027F484D93A0, junto com o snapshot do valor de x naquele momento.
# A seguir, 'action' recebe o endereço de fun2 + snapshot.
# E, se testarmos, 'action' é realmente uma função (class "function").
action = fun1() # retorno da fun1 é o endereço da fun2.
print('Valor de \'action\'', action) # 0x0000027F484D93A0 Endereço da fun2.
print('\'action\' é função:', type(action)) # <class 'function'> action é função.
action() # executa a fun2 com o snapshot do escopo. 66 é impresso, mesmo com o escopo "oficial" da fun1 fora da memória.

def calcula_preco_final(valor, tipo_de_cliente):
    dic = {
        'premium': (0.10 if valor <= 1000 else 0.12),
        'básico': 0.05}
    return valor * (1 - dic.get(tipo_de_cliente))

preco1 = 1000
print('Preço 1 Cheio: R$', preco1)
print('Preço 1 Usuário Básico:', calcula_preco_final(preco1, 'básico'))
print('Preço 1 Usuário Premium:', calcula_preco_final(preco1, 'premium'))
preco2 = 2000
print('Preço 2 Cheio: R$', preco2)
print('Preço 2 Usuário Básico:', calcula_preco_final(preco2, 'básico'))
print('Preço 2 Usuário Premium:', calcula_preco_final(preco2, 'premium'))

# experiências com mutable / unmmutable
x = 10
y = x
print('id(x) =', id(x)) # 140705930544328
print('id(y) =', id(y)) # 140705930544328
x += 5 # immutable => new memory address
print('id(x) =', id(x)) # 140705930544488
print('id(y) =', id(y)) # 140705930544328
print(x, y) # 15 10

x = 'abc'
y = x
print('id(x) =', id(x)) # 2038661676560
print('id(y) =', id(y)) # 2038661676560
x = 'def' # immutable => new memory address
print('id(x) =', id(x)) # 2038662273168
print('id(y) =', id(y)) # 2038661676560
print(x, y) # def abc

x = ['abc']
y = x
print('id(x) =', id(x)) # 2370111382528
print('id(y) =', id(y)) # 2370111382528
x[0] = 'def' # mutable => x remains at same memory address
print('id(x) =', id(x)) # 2370111382528
print('id(y) =', id(y)) # 2370111382528
print(x, y) # ['def'] ['def']
