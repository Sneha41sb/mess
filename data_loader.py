#pandas for real dataset
import pandas as pd
df=pd.read_csv('data.csv') # load dataset
print(df.head()) #first 5 rows
print(df.shape())#rows and columns
print(df.info())#info
print(df.describe())#mean,min,max etc for num columns