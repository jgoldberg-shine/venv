import matplotlib.pyplot as plt



df = df.sort_values("Responses")    #Display the bars in different order

bar_colours = ['red' if x=df["Responses"].max() else 'blue' for x in df["Responses"]] #to change bar colour

plt.bar("Locations", "Responses", data=df)  #plot a bar chart from a df
plt.show()

plt.barh("Locations", "Responses", data=df) #plot horizontal chart
plt.show()

df = df.sort_values("Responses")    #


my_plot = df.plot.barh(stacked=True)    #create a stacked horizontal bar chart
df = df.T   #to transpose the data and switch the columns and index

plt.pie(employees, labels=roles, autopct="%.1f%%")    #to create a pie chart with % labels
explode=[0.2,0,0,0]     #to explode a section of the pie chart, the values state how far the secctio should move away
ply.show()

plt.scatter(number_of_placements, responses_received)   #to create a scatter graph
plt.show()

plt.xlabel("Number of places advertisded")
plt.ylabel("Responses Received")
plt.title("Job Posting - Junior Dev Role")

number_or_placements = np.array(range(1,11)) #to create a line of best fit
responses_received = np.array([14, 21, 24, 36, 45, 51, 54, 63, 78, 92])

a,b = np.polyfit(number_or_placements, responses_received, 1)   #work out the slope of the line


