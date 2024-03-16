# sunday: 
# Debit            23      
# Cash             14      
# Credit            4      
# Mobile Wallet     2      
# Voucher           2  

# monday:

# Payment Method
# Debit            20
# Mobile Wallet     8
# Cash              6
# Credit            5
# Voucher           3

# tuesday:

# Debit            26
# Cash             15
# Credit            9
# Voucher           6
# Mobile Wallet     2

# wednesday:

# Debit            19
# Cash             17
# Credit            8
# Mobile Wallet     7
# Voucher           7

# thursday:

# Debit            26
# Credit           15
# Cash             13
# Mobile Wallet     3
# Voucher           2

# friday:
# Debit            27
# Cash             17
# Credit           11
# Voucher           5
# Mobile Wallet     3

# saturday:
# Cash             20
# Debit            17
# Credit           12
# Voucher           8
# Mobile Wallet     5

import matplotlib.pyplot as plt

# Define the data
data = {
    'Sunday': {'Debit': 23, 'Cash': 14, 'Credit': 4, 'Mobile Wallet': 2, 'Voucher': 2},
    'Monday': {'Debit': 20, 'Mobile Wallet': 8, 'Cash': 6, 'Credit': 5, 'Voucher': 3},
    'Tuesday': {'Debit': 26, 'Cash': 15, 'Credit': 9, 'Voucher': 6, 'Mobile Wallet': 2},
    'Wednesday': {'Debit': 19, 'Cash': 17, 'Credit': 8, 'Mobile Wallet': 7, 'Voucher': 7},
    'Thursday': {'Debit': 26, 'Credit': 15, 'Cash': 13, 'Mobile Wallet': 3, 'Voucher': 2},
    'Friday': {'Debit': 27, 'Cash': 17, 'Credit': 11, 'Voucher': 5, 'Mobile Wallet': 3},
    'Saturday': {'Cash': 20, 'Debit': 17, 'Credit': 12, 'Voucher': 8, 'Mobile Wallet': 5}
}

# Extract payment methods and days
payment_methods = set()
days = list(data.keys())

for day_data in data.values():
    payment_methods.update(day_data.keys())

payment_methods = sorted(payment_methods)

# Create lists for each payment method
debit = [data[day].get('Debit', 0) for day in days]
cash = [data[day].get('Cash', 0) for day in days]
credit = [data[day].get('Credit', 0) for day in days]
mobile_wallet = [data[day].get('Mobile Wallet', 0) for day in days]
voucher = [data[day].get('Voucher', 0) for day in days]

# Create the grouped bar chart
bar_width = 0.15
index = range(len(days))

plt.figure(figsize=(12, 6))

plt.bar(index, debit, bar_width, label='Debit')
plt.bar([i + bar_width for i in index], cash, bar_width, label='Cash')
plt.bar([i + 2 * bar_width for i in index], credit, bar_width, label='Credit')
plt.bar([i + 3 * bar_width for i in index], mobile_wallet, bar_width, label='Mobile Wallet')
plt.bar([i + 4 * bar_width for i in index], voucher, bar_width, label='Voucher')

plt.xlabel('Days')
plt.ylabel('Transactions')
plt.title('Transactions by Payment Method')
plt.xticks([i + 2 * bar_width for i in index], days)
plt.legend()

plt.tight_layout()
plt.savefig("groupedbarchart.png")
plt.show()
