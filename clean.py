import pandas as pd

df = pd.read_csv("final_stars.csv")

print(df.columns)

df.drop(["Unnamed: 0"], axis = 1, inplace=True)

print(df.columns)

data = df.dropna()

print(data)

data.reset_index(drop = True, inplace = True)

print(data)

data.to_csv("final_stars.csv")

df = pd.read_csv("final_stars.csv")

print(df[1])



