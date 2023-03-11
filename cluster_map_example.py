# https://www.youtube.com/watch?v=FX9cW1bOiV8&t=985s
# pip install folium
# pip install pandas

import folium
import pandas as pd

df = pd.read_csv('points.csv')
df.columns = df.columns.str.strip()
df.head()

subset_of_df = df.sample(n=8)
some_map = folium.Map(location=[subset_of_df[NORT_LATITUDE].mean(),
                       subset_of_df[WEST_LATITUDE].mean()],
                       zoom_start=10)