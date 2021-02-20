import csv
import pandas as pd
df = pd.read_csv('coviddataset.csv', usecols=['Country_Region'])
df_noDuplicates=df.drop_duplicates() #remove duplicates
print(df_noDuplicates.head(len(df_noDuplicates)))
d_list = df_noDuplicates.to_dict()  #convert to list
print(d_list)
