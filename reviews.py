import os
import zipfile
import pandas as pd

df_wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip", compression="zip", index_col=2)
df_wine_countries_count_points = df_wine_reviews.groupby("country").agg({"country" : "count","points" : "mean"}).round(1)
df_wine_countries_count_points = df_wine_countries_count_points.rename(columns={'country' : 'count'}).reset_index()
df_wine_countries_summary = df_wine_countries_count_points.sort_values("count", ascending=False)

#df_wine_countries_summary
#a dataframe requires an index (default or not), the index can be removed/hidden in the function where you are writing to a file.

#to write file to different folder from file directory
path = 'C:/Users/Aliyah Gant/Documents/Projects/wine-reviews-exercise-amgant/data'
output_file = os.path.join(path,'reviews-per-country.csv')

df_wine_countries_summary.to_csv(output_file, index=False)

