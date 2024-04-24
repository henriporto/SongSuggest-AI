# Module to generate song recommendations

# TODO

# get user's favorite songs.
# If input IDs in dataset -> get features from dataset['features']
# If input = Name of songs or artists:
    # Try to find them in dataset and get all features from dataset['features'].
    # If we can't find the songs, get all data from https://genius.com/ and create features for each.

# Compare users features with all dataset features (using 'cosine similarity' or other method) and get top N similar songs.