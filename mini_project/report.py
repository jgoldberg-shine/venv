import pandas as pd
from ydata_profiling import ProfileReport

df=pd.read_excel("alldays_exploded.xlsx")

profile = ProfileReport(df, title = "MegaBytes Results") #create a new ProfileReport object

profile.to_file('MegaBytes_report_exploded.html') #export to html file