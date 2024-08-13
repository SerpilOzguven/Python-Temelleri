import pandas as pd

df = pd.read_csv("data/imdb.csv")

result = df
result = df.columns
result = df.info


print(result)
