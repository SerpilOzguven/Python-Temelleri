import pandas as pd


df = pd.read_csv("youtube-ing.csv")

result = df

#1- ilk 10 kaydı getiriniz.
result = df.head(10) 

#2- ikinci 5 kaydı getiriniz.
result =df[5:10].head()

#3 Datasette bulunan kolon isimleri ve sayısını bulalım
result = (df.columns).value_counts


print(result)
