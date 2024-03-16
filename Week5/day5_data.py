import pandas as pd

df = pd.read_csv("results.csv")

df.info()

print(df.describe())

print(df["home_score"].value_counts(normalize=True)*100) #views each score as a % of the total 

mask = df['home_score'] > 6 #removed values above 6 goals
df = df[~mask]
print(df["home_score"].mean()) #calculate mean again to check differnce
