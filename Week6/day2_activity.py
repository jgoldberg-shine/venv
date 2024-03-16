import pandas as pd

df = pd.read_excel("cleaning_activity.xlsx")

#data clean
df = df.drop([0]) #remove first row
df = df.dropna(how = "any") #remove any rows with NaN values
df = df.drop_duplicates() #remove any duplicate rows

#question 1
print(df["Staff"].value_counts()) #view list of entries in 'staff' column

def staff_lowercase (employee):
    employee = str(employee)
    return employee.lower()

df["Staff"] = df["Staff"].apply(staff_lowercase)

print(df["Staff"].value_counts())
print(df["Staff"].mode())
