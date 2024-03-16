import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_csv("results.csv")

profile = ProfileReport(df, title = "International Results") #create a new ProfileReport object

profile.to_file('results_report.html') #export to html file