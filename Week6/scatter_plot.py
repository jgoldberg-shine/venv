import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

number_of_placements = list(range(1,11))
responses_received = [14, 21, 34, 36, 45, 51, 54, 63, 78, 92]


plt.scatter(number_of_placements, responses_received)   #to create a scatter graph


number_of_placements = np.array(range(1,11)) #to create a line of best fit
responses_received = np.array([14, 21, 34, 36, 45, 51, 54, 63, 78, 92])

a,b = np.polyfit(number_of_placements, responses_received, 1)   #work out the slope of the line
plt.plot(number_of_placements,a*number_of_placements+b)


plt.xlabel("Number of places advertisded")
plt.ylabel("Responses Received")
plt.title("Job Posting - Junior Dev Role")

plt.show()


# 14, 21, 34, 36, 45, 51, 54, 63, 78, 92
# 14, 21, 34, 50, 70, 90