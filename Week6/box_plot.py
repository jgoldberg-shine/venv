import pandas as pd
import matplotlib.pyplot as plt

dev_ages=[
        45, 23, 57, 27, 37, 39, 61, 48, 23, 27, 
        59, 60, 28, 41, 25, 39, 22, 46, 48, 52, 
        38, 41, 52, 30, 46, 62, 25, 34, 52, 35, 
        48, 43, 21, 40, 22, 22, 57, 25, 21, 30, 
        55, 50, 54, 30, 43, 40, 53, 46, 36, 61, 
        35, 39, 40, 31, 29, 65, 28, 57, 39, 36, 
        20, 49, 42, 29, 62, 52, 29, 57, 39, 32
        ]

plt.boxplot(dev_ages, vert=0)   #vert=0 makes the plot horizontal
plt.show()

# plt.hist(dev_ages, edgecolor="black")
# bins=[20,25,30,35,40,45,50,55,60,65]    #specify the bin sizes(ranges)
# plt.show()

# plt.savefig("dev_age_plot_hist.png")