import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data acquisition, intake conversion path
df = pd.read_csv('path.csv')
cols = df.columns

# Attribution Analysis
# 1st-touch method, locate 1st touch
df['1st_touch']= df['path'].map(lambda x: x.split('~')[0])

# create a df for 1st touch
df_ft = pd.DataFrame()
# credit attribution to 1st touch in the new df
df_ft['channel'] = df['1st_touch']
df_ft['attribution'] = 'First Touch'
df_ft['conversion'] = 1

# last-touch method
df['last_touch']= df['path'].map(lambda x: x.split('~')[-1])
df_lt= pd.DataFrame()
df_lt['channel'] = df['last_touch']
df_lt['attribution'] = 'last Touch'
df_lt['conversion'] = 1

# which channel has more conversions in first-touch method? or in last-touch method
# group by
df_ft = df_ft.groupby(['channel','attribution']).sum().reset_index()
df_lt = df_lt.groupby(['channel','attribution']).sum().reset_index()

# combine the graph
df = pd.concat([df_ft,df_lt])
#df.sort_values(by='channel', inplace=True, ascending=True)
sns.barplot(data = df, x='channel', y = 'conversion', hue='attribution')
plt.show()

# First touch shows channel 10 has the most number of conversions.
# Last touch shows channel 21 has the most number of conversions.
