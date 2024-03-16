import pandas as pd
import numpy as np

languages = pd.Series(["python", "JavaScript", "HTML", "SQL"])

ranking = pd.Series([3, 1, 2, 4])


df = pd.DataFrame({
    "languages": languages,
    "ranking" : ranking
})

df.loc[4] = ["PHP", 11]
df.loc[3.5] = ["KESL", 20]
df = df.sort_index()
df = df.reset_index(drop = True)

# new_data = pd.DataFrame({"languages": ["PHP"], "ranking": [11]})
# df = pd.concat([df, new_data], ignore_index=True)
print(df)


# df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)])
# df.columns = ["Name", "Age"]
# print(df)

# df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)],
#                   columns = ["Name", "Age"])
# print(df)



# df = pd.read_csv("speeds.csv")

# df = pd.read_excel("speeds.xlsx")
# print(df)

# name = pd.Series(["Mercury", "Venus", "Earth", "Mars"])
# temp = pd.Series([167, 464, 15, -65])
# radius = pd.Series([2439, 6051, 6371, 3389])
# colour = pd.Series(["grey", "orange/red", "blue/green", "red"])
# feature = pd.Series(["smallest planet", "a day is longer than a year", "only place we know that can support life", "once had an atmosphere like Earth"])

# df = pd.DataFrame({
#     "Name" : name,
#     "Average temp (degC)" : temp,
#     "Radius" : radius,
#     "Planet colour" : colour,
#     "Interesting feature" : feature
# })

# print(df)

# file_name = 'PlanetData.xlsx'

# df.to_excel(file_name)
