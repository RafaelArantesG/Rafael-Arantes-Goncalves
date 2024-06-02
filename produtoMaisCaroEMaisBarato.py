#Three lines to make our compiler able to draw:
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

### Leio os dados do arquivo original. Durante a leitura, aproveito somente as colunas que podem me interessar.
df = pd.read_csv('Sanitized.csv', 
                    delimiter=",", 
                    header="infer",
                    usecols=['Product Category', 'Product Price']
                )

### ordeno pelo valor menor
df2 = df.sort_values('Product Price')

print('Produto Mais Barato: ')
print(df2.head(1))

print('Produto Mais Caro: ')
print(df2.tail(1))
