import pandas as pd

file_path = 'song_lyrics.csv'

pd.set_option('display.max_colwidth', None)
df = pd.read_csv(file_path, usecols=['lyrics'], nrows=3)

print(df)
