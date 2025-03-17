# O resultado dos dois prints são [1] e [1,1].
def func(data=[]):
    data.append(1)
    return data

print(func())
print(func())