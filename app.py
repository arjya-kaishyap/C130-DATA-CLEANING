import pandas as pd
import csv
df=pd.read_csv('main.csv')
#del df['hyperlink']
del df['Star Name']
del df['Distance (ly)']
del df['Mass(MJ)']
del df['Radius (RJ)']
print(df.shape)
print(list(df))
df.to_csv('main2.csv')