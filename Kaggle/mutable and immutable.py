# relembrando o conceito de mutabilidade (list) e imutabilidade (tuple)
# tanto faz mexer na L1 ou L2. Dá no mesmo
L1 = [1,2,3]
L2 = L1
print(L1, id(L1), L2, id(L2)) # [1, 2, 3] 2151710733440 [1, 2, 3] 2151710733440
L1.append(4)
print(L1, id(L1), L2, id(L2)) # [1, 2, 3, 4] 2151710733440 [1, 2, 3, 4] 2151710733440
L2.append(5)
print(L1, id(L1), L2, id(L2)) # [1, 2, 3, 4, 5] 2151710733440 [1, 2, 3, 4, 5] 2151710733440
# Mexer na T1 não causa mudança na T2
T1 = (1,2,3)
T2 = T1
print(T1, id(T1), T2, id(T2)) # (1, 2, 3) 2746646931456 (1, 2, 3) 2746646931456
T1 = (1,2,3,4)
print(T1, id(T1), T2, id(T2)) # (1, 2, 3, 4) 2746646969328 (1, 2, 3) 2746646931456