# Dicionário de 3 chaves usado no exemplo
dic1 = {'marca':'Citroen', 'modelo':'C3', 'ano':'2024'} # Estado inicial do dicionário.
print('Estado original do dicionário:', dic1, '- com', len(dic1), 'chaves.\n')

print('====== Exemplo 1 - Chave não existe e será adicionada'.upper(), '======')

print('Valor da nova chave \'único dono\':', dic1.setdefault('único dono', 'Sim'))
print('Estado final do dicionário:', dic1, '- com', len(dic1), 'chaves.')

print('\n====== Exemplo 2 - Chave já existe e será ignorada'.upper(), '======')
print('Estado atual do dicionário:', dic1)
print('Valor original da chave \'modelo\' é preservado:', dic1.setdefault('modelo', 'C4'))
print('Estado final do dicionário:', dic1)
dic2={'a':2}

