import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

# print(df.describe())

df = df.set_index("Transaction ID")

df = df.drop(columns=["Till ID"])
df = df.drop([16,17,18])
df = df.drop_duplicates()
df.at[12,"Amount"] = 3.10

def float_to_time(stamp):
    stamp = str(stamp)
    stamp = stamp.replace(".", ":")
    stamp = "0" + stamp
    if len(stamp) != 5:
        stamp = stamp + "0"
    return stamp

df["Time"] = df["Time"].apply(float_to_time)
df["Time"] = pd.to_datetime(df["Time"])

# print(df)

# print(df.describe())

#activity 1 - average price of an item

item_total = df["Items"].sum()
amount_total = df["Amount"].sum()

average_item = amount_total/item_total

print(average_item)

#activity 2 - average basket price

mean_price = df["Amount"].mean()

print(mean_price)

#activity 3 - max spend in one transaction

max_spend = df["Amount"].max()
print(max_spend)

#activity 4 - min spend in one transaction

min_spend = df["Amount"].min()
print(min_spend)
#activity 5 - most common spend amount

mode_spend = df["Amount"].mode()
print(mode_spend)

#activity 6 - most common payment type

mode_payment = df["Currency"].mode()
print(mode_payment)

print(df["Currency"].mode()[0])