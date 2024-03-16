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

# Aggregate data across all days
total_data = {}
for day_data in data.values():
    for payment_method, value in day_data.items():
        total_data[payment_method] = total_data.get(payment_method, 0) + value

# Plotting the pie chart
labels = total_data.keys()
sizes = total_data.values()
explode = (0, 0, 0, 0, 0.1)  # explode 4th slice (Voucher)

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Payment Types Distribution Over All Days')
plt.show()
# plt.savefig("piechart.png")
