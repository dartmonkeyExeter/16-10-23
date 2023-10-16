# electric boogaloo
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

pd.set_option('display.max_rows', None)

df = pd.read_csv('spotify-2023.csv', encoding="ISO-8859-1")

pluh = pd.pivot_table(df, values='streams',index='artist(s)_name',aggfunc=np.sum)
print(pluh)

pluh = pd.pivot_table(df, values='danceability_%', index='released_month', aggfunc=np.mean)
print(pluh)

pluh = pd.pivot_table(df, values='streams', index='key', aggfunc='max')
print(pluh)

pluh = pd.pivot_table(df, values='energy_%', index='mode', aggfunc=np.mean)
print(pluh)

pluh = pd.pivot_table(df, values='valence_%', index='released_year', aggfunc=np.sum)
print(pluh)

pluh = pd.pivot_table(df, values='speechiness_%', index='artist(s)_name', aggfunc='max')
print(pluh)
pluh = pd.pivot_table(df, values='speechiness_%', index='artist(s)_name', aggfunc='min')
print(pluh)

pluh = pd.pivot_table(df, index=['artist(s)_name'], columns=['released_month'], values=['track_name'], aggfunc='count')
print(pluh)

pluh = pd.pivot_table(df, values='streams', index='artist_count', columns='released_year', aggfunc='mean')
print(pluh)

pluh = pd.pivot_table(df, values=['danceability_%', 'energy_%'], index='key', columns='mode', aggfunc='mean')
print(pluh)

pluh = pd.pivot_table(df, values=['in_spotify_playlists', 'in_apple_playlists'], index='released_month', columns='released_day', aggfunc='max')
print(pluh)

pattern = r'^\\d{2}$'
filtered_df = df[df['artist(s)_name'].astype(str).str.match(pattern)]
unique_artists = filtered_df['artist(s)_name'].unique()
print(unique_artists)
