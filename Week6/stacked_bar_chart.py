# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.DataFrame({
#     "Engineering":[56,13,1],
#     "Computer Science":[77,23,4],
#     "English Lit":[35,48,9],
#     "Economics": [65,45,19]
# }, index=["Male", "Female", "Non-Binary"])

# df = df.T   #to transpose the data and switch the columns and index
# my_plot = df.plot.barh(stacked=True)    #create a stacked horizontal bar chart

# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.DataFrame({
    "Engineering": [56, 13, 1],
    "Computer Science": [77, 23, 4],
    "English Lit": [35, 48, 9],
    "Economics": [65, 45, 19]
}, index=["Male", "Female", "Non-Binary"])

df = df.T  # Transpose the data

# Create a stacked horizontal bar chart
my_plot = df.plot.barh(stacked=True, figsize=(10, 6))

# Add percentage values to the bars
for idx, series in enumerate(df.values):
    total = sum(series)
    cum_sum = 0
    for i, value in enumerate(series):
        cum_sum += value
        plt.text(cum_sum - value / 2, idx, f'{value / total:.1%}', va='center', ha='center', color='white')

plt.xlabel('Number of Students')
plt.ylabel('Subjects')
plt.title('Number of Students by Subject and Gender')
plt.legend(title='Gender')
plt.show()
