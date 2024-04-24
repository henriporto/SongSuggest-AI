import pandas as pd

file_path = 'song_lyrics.csv'

max_lengths = []
min_lengths = []
median_lengths = []

chunk_size = 500000 

for chunk in pd.read_csv(file_path, usecols=['lyrics'], chunksize=chunk_size):

    chunk['length'] = chunk['lyrics'].str.len()

    max_lengths.append(chunk['length'].max())
    min_lengths.append(chunk['length'].min())
    median_lengths.append(chunk['length'].median())


    print(f"Processing chunk: Max length = {max_lengths[-1]}, Min length = {min_lengths[-1]}, Median length = {median_lengths[-1]}")

print("\nFinal Lengths Summary:")
print("All Max Lengths:", max_lengths)
print("All Min Lengths:", min_lengths)
print("All Median Lengths:", median_lengths)