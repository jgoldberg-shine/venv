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
    "Totals by payment types": [
        "Voucher",
        "Cash",
        "Debit",
        "Credit",
        "Mobile"
    ],
    "Amount": [228, 684, 1117, 429, 173],
})

df = df.sort_values("Amount")  # Display the bars in different order

# Define colors for bars
bar_colors = ['red' if payment_type == 'Voucher' else 'blue' for payment_type in df['Totals by payment types']]

plt.bar("Totals by payment types", "Amount", data=df, color=bar_colors)  # Plot a bar chart from a df

# Annotate each bar with its value
for i, value in enumerate(df['Amount']):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.xlabel('Payment Type')  # Label for x-axis
plt.ylabel('Amount in £')  # Label for y-axis
plt.title('Total Spending by Payment Type Over One Week')  # Title for the plot

plt.show()
# plt.savefig("barchart1.png")