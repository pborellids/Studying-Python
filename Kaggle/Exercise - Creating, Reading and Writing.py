import pandas as pd

# Options:
# 'display.max_rows'
# 'display.precision'
# 'display.max_colwidth'
# 'display.max_columns'
pd.set_option('display.max_rows', 5)

# DataFrame criado a partir de dicionário. É necessário que os valores estejam na forma de lista.
fruits = {
    'Apples': [30],
    'Bananas': [21]
}
df = pd.DataFrame(fruits)
print(df)
print()

# O mesmo DataFrame criado diretamente no método "DataFrame".
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
print(fruits)

fruit_sales = {
    'Apples': {'2017 Sales': 35, '2018 Sales': 41},
    'Bananas': {'2017 Sales': 21, '2018 Sales': 34}
}
df = pd.DataFrame(fruit_sales)
print(df)

fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'], index=['2017 Sales', '2018 Sales'])
print('\n', fruit_sales, '\n')

quantities = ['4 cups', '1 cup', '2 large', '1 can']
items = ['Flour', 'Milk', 'Eggs', 'Spam']
recipe = pd.Series(quantities, index=items, name='Dinner')
print(recipe)


