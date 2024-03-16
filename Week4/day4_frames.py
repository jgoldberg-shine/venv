import pandas as pd
import numpy as np

# languages = pd.Series(["python", "JavaScript", "HTML", "SQL"])

# ranking = pd.Series([3, 1, 2, 4])


# df = pd.DataFrame({
#     "languages": languages,
#     "ranking" : ranking
# })

# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]
# df.loc[5] = ["Java", 7]
# df.loc[6] = ["TypeScript", 5]
# df = df.sort_index()
# df = df.reset_index(drop = True)

# df["ranking 2022"]=[4,1,2,3,10,6,5,5]

# print(df.columns.get_loc("ranking 2022"))

# # new_data = pd.DataFrame({"languages": ["PHP"], "ranking": [11]})
# # df = pd.concat([df, new_data], ignore_index=True)
# print(df)

# Activity

name = pd.Series(["Mercury", "Venus", "Earth", "Mars"])
temp = pd.Series([167, 464, 15, -65])
radius = pd.Series([2439, 6051, 6371, 3389])
colour = pd.Series(["grey", "orange/red", "blue/green", "red"])
feature = pd.Series(["smallest planet", "a day is longer than a year", "only place we know that can support life", "once had an atmosphere like Earth"])

df = pd.DataFrame({
    "Name" : name,
    "Average temp (degC)" : temp,
    "Radius" : radius,
    "Planet colour" : colour,
    "Interesting feature" : feature
})

df["Who discovered it?"] = ["Galileo", "Gelileo", "N/A", "Galileo"]
df["Year of discovery"] = [1631, 1610, "N/A", 1610]
df["Composition"] = ["Fe, Si", "Si, Al, Mg", "O2, Si, Al, Ca, Na...", "Si, O2, Fe, Mg, Al"]

df.loc[4] = ["Pluto", -232, 1151, "white and brownish-red", "no longer a planet", "Clyde Tombaugh", 1930, "N2, CH4, CO"]

# df = df.set_index("Name")

print(df)
print(df[["Name", "Composition"]])

print(df.loc[3])

file_name = 'PlanetData2.xlsx'

df.to_excel(file_name)

print(df.iloc[1:3])
df = df.set_index("Name")

planet_selected  = input("Which planet would you like information on?: ")

for i in df.columns:
    print (i)

column_select = input("Which column would you like to see? Type 'all' to see all: ")

if column_select == "all":
    print (df.loc[f"{planet_selected}"])

else:
    print(df.loc[planet_selected, column_select])
