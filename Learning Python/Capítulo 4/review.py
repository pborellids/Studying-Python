# sequences are ORDERED sets: strings, lists and tuples. Lists are mutable. Strings and Tuples aren't.

L = [1, 2, 3, 4, 4]
print(type(L))
print(type(type(L)))
print(type(L) == type([])) # True
print(type(L) == list)

s = "abc"
s1 = s
print(s,s1)
s1="abcd"
print(s,s1)

L = [1,2,3,4]
L2 = L
print(L,L2)
L.append(4)
print(L,L2)
L.append((10,11,12))
print(L,L2)
