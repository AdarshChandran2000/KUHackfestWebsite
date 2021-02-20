import csv
import pandas as pd
df = pd.read_csv('coviddataset.csv', usecols=['Country_Region'])
df_noDuplicates=df.drop_duplicates()
print(df_noDuplicates.head(len(df_noDuplicates)))
