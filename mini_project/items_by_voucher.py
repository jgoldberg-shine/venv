import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
df = pd.read_excel('alldays_exploded.xlsx')

voucher_df = df[df['Payment Method'] == 'Voucher']
# voucher_df.to_excel ('voucheritems.xlsx')

print(voucher_df['Basket'].value_counts())

df = pd.DataFrame({
    "Items paid for by Voucher" : [
    "Cappuccino",
    "Latte",
    "Mocha",
    "Hot Chocolate",
    "Americano",
    "Tea",
    "Buttered Roll",
    "Muffin",
    "Toast",
    "Stroopwafel",
    "Panini",
    "Croissant"
],
    "Amount" : [26, 24, 24, 17, 14, 13, 2, 2, 1, 1, 1, 1],
})

df = df.sort_values("Amount")    #Display the bars in different order

bar_colours = ['red' if x==df["Amount"].max() else 'blue' for x in df["Amount"]] #to change bar colour

plt.bar("Items paid for by Voucher", "Amount", data=df)  #plot a bar chart from a df
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.xlabel('Items paid for by Voucher')  # Label for x-axis
plt.ylabel('Amount')  # Label for y-axis
plt.title('Items paid for by Voucher')  # Title for the plot

plt.show()

# plt.savefig("itemsbyvouchers.png")