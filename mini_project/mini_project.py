import pandas as pd    
import matplotlib.pyplot as plt
df1 =pd.read_excel ('monday_graph.xlsx')
df2 =pd.read_excel ('tuesday_graph.xlsx')
df3 =pd.read_excel ('wednesday_graph.xlsx')
df4 =pd.read_excel ('thursday_graph.xlsx')
df5 =pd.read_excel ('friday_graph.xlsx')
df6 =pd.read_excel ('saturday_graph.xlsx')
df7 =pd.read_excel ('sunday_graph.xlsx')
dfs=[df1,df2,df3,df4,df5,df6,df7]
aggregate=pd.concat(dfs, ignore_index=True)
aggregate.to_excel('aggregate.xlsx')

excel_files = ['aggregate.xlsx']


for file in excel_files:
    print(f"Day: {file}")
    
    # Read the Excel file
    df = pd.read_excel(file)
    
    # Drop the first row and remove rows with any NaN values
    df = df.drop([0])
    df = df.dropna(how="any")
    
    # Print the value counts of the "Payment Method" column
    print(df["Payment Method"].value_counts())
    
    # Define function to remove punctuation
    def remove_punctuation(basket):
        basket = str(basket)
        basket = basket.replace("[", "")
        basket = basket.replace("]", "")
        basket = basket.replace("'", "")
        return basket
    
    # Apply the remove_punctuation function to the "Basket" column
    df["Basket"] = df["Basket"].apply(remove_punctuation)
    
    # Define function to split basket string into a list
    def split_basket(basket_str):
        elements = basket_str.split(",")
        return [item.strip() for item in elements]
    
    # Apply the split_basket function to the "Basket" column
    df["Basket"] = df["Basket"].apply(split_basket)
    
    # Explode the "Basket" column to create separate rows for each item in the basket
    df = df.explode("Basket", ignore_index=False)
    
    # Print the value counts of the "Basket" column
    print(df["Basket"].value_counts())
    
    # Print descriptive statistics of the DataFrame
    # print(df.describe())


# df = pd.read_excel("alldays.xlsx")
# print(df["Cost"].sum())

# print(df)


