import pandas as pd
import matplotlib.pyplot as plt
# List of Excel files to iterate through
excel_files = ['monday_graph.xlsx']


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
    print(df.describe())

#     # print(df)
df = pd.DataFrame({
    "Payment Type" : [
    "Debit",
    "Mobile Wallet",
    "Cash",
    "Credit",
    "Voucher"
],
    "Day" : [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ],
    # "Number": [20,8,6,5,3],
})

# df = df.sort_values("Responses")    #Display the bars in different order

# bar_colours = ['red' if x==df["Responses"].max() else 'blue' for x in df["Responses"]] #to change bar colour

plt.bar("Payment Type", "Day" data=df)  #plot a bar chart from a df

plt.show()