import pandas as pd

### Leio os dados do arquivo original. Durante a leitura, aproveito somente as colunas que podem me interessar.
### Posteriormente iremos salvar arquivos já trabalhados, apenas para referência.
df = pd.read_csv('Ecommerce_DBS.csv', 
                        delimiter=",", 
                        header="infer", 
                        usecols=['Purchase Date','Product Category', 'Product Price','Quantity','Total Purchase Amount','NPS','Customer Age ', 'Gender', 'Source']
                    )

### Salvo um arquivo pra ter a referência da base com a qual vou trabalhar. Em caso de necessidade, posso manipular este arquivo diretamente.
df.to_csv('Sanitized.csv', index=False)
