import pandas as pd

file_path = 'song_lyrics.csv'

total_rows = 0

# Process the file in chunks
for chunk in pd.read_csv(file_path, chunksize=100000):  # Adjust chunksize based on your system's memory
    total_rows += len(chunk)

print(total_rows)
