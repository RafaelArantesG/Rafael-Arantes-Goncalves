import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

### Leio os dados do arquivo Sanitizado. Durante a leitura, aproveito somente as colunas que podem me interessar.
df = pd.read_csv('Sanitized.csv', 
                    delimiter=",", 
                    header="infer",
                    usecols=['Product Category', 'NPS']
                )

### Agrupo por categoria de produtos calculando o menor e o maior NPS
df2 = df.sort_values('NPS')

print('O produto com pior NPS é: ')
print(df2.head(1))

print('O produto com melhor NPS é: ')
print(df2.tail(1))
