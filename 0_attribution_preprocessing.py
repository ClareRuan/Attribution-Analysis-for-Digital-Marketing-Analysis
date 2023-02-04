# importing pandas module
import pandas as pd

# data acquisition, reading csv file
df = pd.read_csv('attribution_channel.csv')
cols = df.columns

# EDA
print(df.shape)
print(df.dtypes)
print(df.head())
print(cols)
#print(df['Output'].unique())

# ETL, data preprocess
# converting dtypes using astype
for col in cols:
    df[col]=df[col].astype(str)
    df[col]=df[col].map(lambda x: str(x)[:-2] if '.' in x else str(x))

df['path']=''
#i_list = ''
# iteration method 1
#for i in df.index:
#   i_list = i_list + ' '+ str(i)

# iteration method 2
#for r in df.iterrows():
#   i_list = i_list + ' ' + str(r[0])

# format clickpath
for i in df.index:
    for x in cols:
        df.at[i, 'path'] = df.at[i, 'path'] + df.at[i,x] + '~'
print(df['path'])

# add one more column in dataframe
df['conversion'] = 1
df = df[['path','conversion']]

# group by duplicated clickpath
df = df.groupby('path').sum().reset_index()
print(df)

# export clickpath with conversion
df.to_csv('path.csv',index=False)

#print(i_list)