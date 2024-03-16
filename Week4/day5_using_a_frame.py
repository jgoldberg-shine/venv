import pandas as pd
import numpy as np

# # df = pd.read_csv("spotify_songs.csv")

# # print(df.shape)
# # print(df.columns)
# # print(df.head)
# # print(df["playlist_genre"].value_counts())
# # print(df["playlist_genre"].mode())
# # print(df["playlist_genre"].mode()[0])
# # print(df["duration_ms"].median())
# # print(df["duration_ms"].mean())

# # max_ms = df["duration_ms"].max()
# # min_ms = df["duration_ms"].min()
# # print(max_ms-min_ms)

# # print(df["duration_ms"].sum())

# # print(df.groupby("playlist_genre")["duration_ms"].min())



# # # print(df.query("track_artist == 'Ricky Martin'"))

# # mean_val = df["duration_ms"].mean()

# # print(df.query("duration_ms > @mean_val"))

# #Activity 1

# # Read and store content 
# # of an excel file 
# read_file = pd.read_excel ("results2024-2-23-110.xlsx") 

# # Write the dataframe object 
# # into csv file 
# read_file.to_csv ("Test.csv", 
# 				index = None, 
# 				header=True) 
	
# # read csv file and convert 
# # into a dataframe object 
# df = pd.DataFrame(pd.read_csv("Test.csv")) 

# df = pd.read_csv("Test.csv")

# #median and mean
# print(df["Download (Mb/s)"].median())
# print(df["Download (Mb/s)"].mean())
# print(df["Upload (Mb/s)"].median())
# print(df["Upload (Mb/s)"].mean())

# #sort by fastest upload

# # print(df.sort_values(by=["Upload (Mb/s)"], ascending=False))


# # #sort by slowest upload
# # print(df.sort_values(by=["Upload (Mb/s)"]))

# # #return download speeds which are faster than the mean
# mean_val = df["Download (Mb/s)"].mean()
# print(mean_val)

# print(df.query("`Download (Mb/s)` > @mean_val"))

#Activity 2
#create a program which displays
#-how many rows and columns
#-name of the columns
#-which cereals have more than 4g of protein
#-all data relating to bran flakes