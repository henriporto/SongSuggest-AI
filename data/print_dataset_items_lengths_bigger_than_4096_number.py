import pandas as pd

file_path = 'song_lyrics.csv'

chunk_size = 500000 
length_threshold = 4096
count_above_threshold = 0

for chunk in pd.read_csv(file_path, usecols=['lyrics'], chunksize=chunk_size):
    chunk['length'] = chunk['lyrics'].str.len()
    count_above_threshold += (chunk['length'] > length_threshold).sum()
    print(f"Processed a chunk. Current count of items with length > {length_threshold}: {count_above_threshold}")

print(f"\nTotal number of items with length greater than {length_threshold}: {count_above_threshold}")
