import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a DataFrame
df = pd.read_excel('alldays.xlsx')

# Filter rows where 'payment method' is 'voucher'
voucher_df = df[df['Payment Method'] == 'Voucher']
cash_df = df[df['Payment Method'] == 'Cash']
debit_df = df[df['Payment Method'] == 'Debit']
credit_df = df[df['Payment Method'] == 'Credit']
mobile_df = df[df['Payment Method'] == 'Mobile Wallet']

# Display the filtered DataFrame
# print(voucher_df)

print(voucher_df["Cost"].sum())
print(cash_df["Cost"].sum())
print(debit_df["Cost"].sum())
print(credit_df["Cost"].sum())
print(mobile_df["Cost"].sum())

df = pd.DataFrame({
    "Payment Type": [
        "Voucher",
        "Cash",
        "Debit",
        "Credit",
        "Mobile"
    ],
    "Amount": [228, 684, 1117, 429, 173],
})

# Define colors for pie chart
pie_colors = ['red', 'blue', 'green', 'orange', 'purple']

# Define explode values
explode = [0.1 if payment_type == 'Voucher' else 0 for payment_type in df['Payment Type']]

plt.pie(df['Amount'], labels=df['Payment Type'], colors=pie_colors, autopct='%1.1f%%', startangle=140, explode=explode)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Total Spending by Payment Type Over One Week')  # Title for the plot

plt.savefig("piechart11.png")
plt.show()

