#Three lines to make our compiler able to draw:
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import timedelta

### Crio uma função de conversão de string para data
def myDateTimeConvert(data):
    return datetime.datetime.strptime(data, '%d/%m/%Y')


### Leio os dados do arquivo Sanitizado. Durante a leitura, aproveito somente as colunas que podem me interessar.
df = pd.read_csv('Sanitized.csv', 
                    delimiter=",", 
                    header="infer",
                    keep_date_col=True,
                    date_parser=myDateTimeConvert,
                    usecols=['Purchase Date', 'Quantity', 'Product Category'],
                    parse_dates=['Purchase Date']
                )

###Calculo a data de 3 anos atrás
now = datetime.datetime.now()
startDate = (now - timedelta.Timedelta(days = (365 * 3) ))

###Executo uma query para encontrar as linhas que atendam ao requisito de estarem nos últimos 3 anos
df2 = df.query('`Purchase Date` >= @startDate')
df3 = df2.groupby(['Product Category']).agg({'Quantity': 'sum'}, ).sort_values('Quantity', ascending=False)
print('O produto mais vendido em quantidade é: ')
print(df3.head(1))
