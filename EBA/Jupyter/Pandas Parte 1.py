import pandas as pd
df = pd.read_csv('EBA\Jupyter\TopSongs20102019ByYear.csv', encoding="ISO-8859-1")
dfs = pd.read_csv('EBA\Jupyter\TopSongsByCountry.csv')
print(df.head())
print()
print(dfs.head())
print()
print('colunas:', df.columns)
print('size:', df.size)
print('shape:', df.shape)
print(df['artist'].nunique())
print()
print(df.describe())
print(df.memory_usage())
print('Músicas com os 3 menores níveis de energia:', df.nsmallest(3, 'nrgy'), sep = '\n')
print()
print('Músicas com os 3 maiores níveis de energia:', df.nlargest(3, 'nrgy'), sep = '\n')
print()
df_ops = df.drop_duplicates(subset=['title'], keep= 'last')
print(df_ops.head())
print('df size:', df.size, 'df_ops size:', df_ops.size)
print()
print(df_ops.sample(n=10))
print()
print('Número de linhas do df_ops:', len(df_ops))

# duas formas de filtrar - query e loc
print()
print('filtro com query:\n', df.query("artist == 'Ariana Grande'"))
print()
print('filtro com loc:\n', df.loc[df['artist'] == 'Ariana Grande'])

# Filtro isin: onde tem uma das duas artistas, os atributos retornam "True". Caso contrário, os atributos aparecem com "false".
print(df.isin(['Ariana Grande', 'Katy Perry']))
# ou:
artistas = ['Ariana Grande', 'Katy Perry']
print(df.isin(artistas)) # todas as entradas são listas, mas os atributos terão valores "false" ou "true" somente,
                         # conforme o atributo coincida com uma das artistas naquela linha.

# Filtro no atributo: dataframe tem alguma linha com artist = 'Queen'? E com artist = 'Ariana Grande'?
print('Queen está no df:', (df['artist'] == 'Queen').any()) # False
print('Ariana Grande está no df:', (df['artist'] == 'Ariana Grande').any()) # True

# removendo uma coluna sem salvar a mudança no dataframe:
print('xxxxxxxxxxxxxxx')
print(df_ops.drop(columns=['spch'])) # coluna spch removida da cópia do dataframe
print('df_ops continua com 15 colunas:', df_ops.shape) # (584, 15)
print(df_ops.head()) # coluna spch continua no dataframe
df_ops.drop(columns=['spch'], inplace=True) # coluna spch removida da cópia e do dataframe.
print(df_ops.head()) # coluna spch realmente removida do dataframe.
print('df_ops ficou com 14 colunas:', df_ops.shape) # (584, 14)

# cálculo de média, mínimo, máximo:
print()
print('Duração Média: %.15f ou %.1f' % (df['dur'].mean(), df['dur'].mean()))
print('Duração Mínima: %.1f' % (df['dur'].min()))
print('Duração Máxima: %.1f' % (df['dur'].max()))

# média e máximo de dois atributos simultaneamente
# Média acous e Máximo dur:
# acous     14.3267
# dur      424.0000
# dtype: float64
print('\nMédia acous e Máximo dur:\n', df.agg({'acous':'mean', 'dur':'max'}), sep = "")

# soma acumulada
print('\nSomas acumuladas de "dur":\n', df['dur'].cumsum(), sep = '')

# ordenando a exibição - ascending = True é default.
print()
print(df_ops.sort_values(by='dur',ascending=False)) # ordem decrescente.
print(df_ops.sort_values(by='dur')) # ordem crescente.

# mudando o atributo "year" para string:
print(df_ops['year'].astype(str))

# colunas "dummies" mostram 1 caso a coluna dummy corresponda ao atributo; 0 em caso contrário.
print()
print(pd.get_dummies(df,columns=['artist']))
#      Unnamed: 0                                              title        top genre  ...  artist_Zedd  artist_fun.  artist_will.i.am
# 0             1                                   Hey, Soul Sister       neo mellow  ...        False        False             False
# 1             2                               Love The Way You Lie  detroit hip hop  ...        False        False             False
# 2             3                                            TiK ToK        dance pop  ...        False        False             False
# 3             4                                        Bad Romance        dance pop  ...        False        False             False
# 4             5                               Just the Way You Are              pop  ...        False        False             False
# ..          ...                                                ...              ...  ...          ...          ...               ...
# 598         599                Find U Again (feat. Camila Cabello)        dance pop  ...        False        False             False
# 599         600      Cross Me (feat. Chance the Rapper & PnB Rock)              pop  ...        False        False             False
# 600         601  No Brainer (feat. Justin Bieber, Chance the Ra...        dance pop  ...        False        False             False
# 601         602    Nothing Breaks Like a Heart (feat. Miley Cyrus)        dance pop  ...        False        False             False
# 602         603                                   Kills You Slowly       electropop  ...        False        False             False

# criando um atributo calculado:
print(df_ops.assign(energy_dance = lambda df: df['dnce'] * df['nrgy']))
#      Unnamed: 0                                              title            artist        top genre  year  ...  val  dur  acous  pop  energy_dance 
# 0             1                                   Hey, Soul Sister             Train       neo mellow  2010  ...   80  217     19   83          5963 
# 1             2                               Love The Way You Lie            Eminem  detroit hip hop  2010  ...   64  263     24   82          6975 
# 2             3                                            TiK ToK             Kesha        dance pop  2010  ...   71  200     10   80          6384 
# 3             4                                        Bad Romance         Lady Gaga        dance pop  2010  ...   71  295      0   79          6440 
# 5             6                                               Baby     Justin Bieber     canadian pop  2010  ...   54  214      4   77          6278 
# ..          ...                                                ...               ...              ...   ...  ...  ...  ...    ...  ...           ... 
# 598         599                Find U Again (feat. Camila Cabello)       Mark Ronson        dance pop  2019  ...   16  176      1   75          4026 
# 599         600      Cross Me (feat. Chance the Rapper & PnB Rock)        Ed Sheeran              pop  2019  ...   61  206     21   75          5925 
# 600         601  No Brainer (feat. Justin Bieber, Chance the Ra...         DJ Khaled        dance pop  2019  ...   65  260      7   70          4028 
# 601         602    Nothing Breaks Like a Heart (feat. Miley Cyrus)       Mark Ronson        dance pop  2019  ...   24  217      1   69          4740 
# 602         603                                   Kills You Slowly  The Chainsmokers       electropop  2019  ...   23  213      6   67          3080 

# [584 rows x 15 columns]

