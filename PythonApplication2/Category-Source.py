#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

### Leio os dados do arquivo original. Durante a leitura, aproveito somente as colunas que podem me interessar.
### Posteriormente iremos salvar arquivos já trabalhados, apenas para referência.
df = pd.read_csv('Sanitized.csv', 
                    delimiter=",", 
                    header="infer"
                )

### Agrupo os dados por Categoria e Gênero para obter os totais de Compras e a média de NPS
df2 = df.get(['Product Category', 'Source', 'Total Purchase Amount', 'NPS'])
df3 = df2.groupby(['Product Category', 'Source']).agg({'Total Purchase Amount': 'sum', 'NPS': 'mean'})
print(df3)

### Gera um gráfico de linha mostrando as quantidades por agrupamento
df3.plot.line(subplots=True, figsize=(25, 15), stacked=False, xlabel='Product Category / Source')
plt.savefig('Category-Source.jpg')

df3.plot.pie(subplots=True, legend=True, figsize=(25, 10))
plt.savefig('Category-Source-pie.jpg')
