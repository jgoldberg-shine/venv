import pandas as pd
import matplotlib.pyplot as plt


roles = [    
    "Front-end", 
    "Back-end",
    "Full-stack",
    "DevOps"
    ]

employees = [52,36,28,11]



plt.pie(employees, labels=roles, autopct="%.1f%%", explode=[0.2,0,0,0] )    #to create a pie chart with % labels
    #to explode a section of the pie chart, the values state how far the secctio should move away
plt.show()