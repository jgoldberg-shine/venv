import matplotlib.pyplot as plt

# years = [2018, 2019, 2020, 2021, 2022, 2023]

# python_position = [7, 4, 4, 3, 4, 3]
# js_position = [1,1,1,1,1,1]
# sql_position = [4, 3, 3, 4, 3, 4]
# type_position = [None, 10, 9, 7, 5, 5]



# plt.title("Most_wanted Language Rating")
# plt.xlabel("Year")
# plt.ylabel("Position")
# plt.ylim(bottom = 10, top = 0) #set limits of y-axis

# plt.plot(years, python_position, label = "Python") #plt.plot to add to the graph from list
# plt.plot(years, js_position, label = "JavaScript", linestyle = "dashed") #linestyle to change the linestyle
# plt.plot(years, sql_position, label = "SQL", linestyle = "dotted")
# plt.plot(years, type_position, label = "Typescript", linestyle = "dashdot")

# plt.legend([          #this list must be written in order so label should be added to plot arguments
    ## "Python",
    ## "JavaScript",
    ## "SQL",
    ## "Typescript"
# ])

# plt.show()

#Activity 1

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Youtube = [2, 1, 3, 6, 3]
Twitter = [1, 1, 0, 0, 2]
WhatsApp =[3, 1, 0, 2, 1]
RaSL = [0, 4, 2, 3, 3]
TikTok = [3, 0, 1, 0, 2]

plt.title("Screen Time")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.ylim(bottom = 0, top = 6) #set limits of y-axis

plt.plot(days, Youtube, label = "YouTube", color = "y")
plt.plot(days, Twitter, label = "Twitter", linestyle = "dashed")
plt.plot(days, WhatsApp, label = "WhatsApp", linestyle = (0, (1,10)))
plt.plot(days, RaSL, label = "Raid: Shadow Legends", linestyle = (0, (3, 10, 1, 10, 1, 10)))
plt.plot(days, TikTok, label = "TikTok", linestyle = (0, (5, 5)))

plt.legend([          #this list must be written in order so label should be added to plot arguments
    "YouTube",
    "Twitter",
    "WhatsApp",
    "Raid: Shadow Legends",
    "TikTok"
])

plt.show()