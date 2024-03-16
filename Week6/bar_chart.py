import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Locations" : [
    "Twitter",
    "Facebook",
    "LinkedIn",
    "Indeed",
    "Instagram"
],
    "Responses" : [3,11,16,13,2],
})

df = df.sort_values("Responses")    #Display the bars in different order

bar_colours = ['red' if x==df["Responses"].max() else 'blue' for x in df["Responses"]] #to change bar colour

plt.bar("Locations", "Responses", data=df, color=bar_colours)  #plot a bar chart from a df

plt.show()

# plt.barh("Locations", "Responses", data=df) #plot horizontal chart
# plt.show()

