import importlib
a = "sou do script.py"
print()
print(a)
print()
import module
# from module import a
print(module.a)
# A ideia agora é alterar a variável "a" no módulo,
# e ver que ela não será alterada neste script. Ou seja,
# o módulo é carregado uma vez apenas durante a execução do programa.
# A biblioteca "importlib" permite recarregar o módulo, reinterpretá-lo inteiramente, atualizando as variáveis.
# input("digite algo:")
print(module.a) # ainda a versão velha da variável "a"
importlib.reload(module) # reinterpretação do módulo
print(module.a) # versão nova da variável "a"
