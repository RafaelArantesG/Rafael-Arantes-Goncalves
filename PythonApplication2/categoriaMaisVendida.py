import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

### Leio os dados do arquivo Sanitizado. Durante a leitura, aproveito somente as colunas que podem me interessar.
df = pd.read_csv('Sanitized.csv', 
                    delimiter=",", 
                    header="infer",
                    usecols=['Quantity', 'Product Category', 'Product Price']
                )

### Agrupo por categoria de produtos calculando a soma das quantidades e o preço médio dos produtos
df2 = df.groupby(['Product Category']).agg({'Quantity': 'sum', 'Product Price': 'mean'})

### Ordeno por quantidade
df3 = df2.sort_values(('Quantity'))

print('A Categoria de Produto menos vendido em quantidade é: ')
print(df3.head(1))

print('A Categoria de Produto mais vendido em quantidade é: ')
print(df3.tail(1))

### Ordeno por preço
df4 = df2.sort_values(('Product Price'))

print('A Categoria de Produto mais Barata é: ')
print(df4.head(1))

print('A Categoria de Produto mais Cara é: ')
print(df4.tail(1))

