import pandas as pd

df = pd.read_excel("cleaning_data.xlsx")

#.drop() to remove columns or row
df = df.drop(columns=["Unnamed: 0", "Till ID"])

df = df.drop([0]) #removes first row

print(df["Transaction Type"].value_counts()) #counts number of times each value in the column appears

df = df.dropna(how="any") #.dropna() to drop any rows with NULL values like NaN

# def replace_item(row):          #if any NULL values are found then returns items in basket as 0 (rather than 3)
#     if row.isna().any():
#         return 0
#     else:
#         return row['Total Items']
    
# df["Total Items"] = df.apply(replace_item, axis=1) #axis=1 performs the operation across the columns which forms the row

def remove_punctuation(basket):     #removing [] and ' punctuation, so that the lists can be read
    basket = str(basket)
    basket = basket.replace("[","")
    basket = basket.replace("]", "")
    basket = basket.replace("'", "")
    return basket

df["Basket"] = df["Basket"].apply(remove_punctuation)

def split_basket(basket_str):       #removes the commas and splits into chunks
    elements = basket_str.split(",")
    return [item.strip() for item in elements]

df["Basket"] = df["Basket"].apply(split_basket)

df = df.explode("Basket", ignore_index=False) #.explode() will open up the list and create a separate row for each item

print(df["Basket"].value_counts())

# def split_basket(basket_str):           #removes the space before the word when printing the list so they can be counted properly
#     elements = basket_str.split(',')    # for evert element in list of elements apply .strip() to it and add it to a new list
#     stripped_elements = [e.strip() for e in elements]
#     return elements

# df["Basket"] = df["Basket"].apply(split_basket)

# print(df)

#activity

