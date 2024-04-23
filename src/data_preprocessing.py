# Module to handle data cleaning and preprocessing

import pandas as pd
import re
import sys
import uuid

# File paths
DATA_FILE_PATH = '../data/song_lyrics.csv'
DATA_DIRECTORY = '../data/'

# Data columns
COLUMNS_TO_NORMALIZE = ['title', 'artist', 'lyrics', 'features', 'tag']

class DataPreprocessor:
    """
    Remove rows with missing values.
    Normalize text fields:
        Conversion to lowercase
        Elimination of extra spaces
    """
    def __init__(self, file_path, columns_to_normalize, language_fields):
        self.file_path = file_path
        self.columns_to_normalize = columns_to_normalize
        self.language_fields = language_fields
        self.data = None

    def load_data(self):
        """ Load data from a CSV file. """
        self.data = pd.read_csv(self.file_path)
        print("Data loaded successfully.")

    def drop_missing_values(self):
        """ Remove rows with missing values. """
        self.data.dropna(inplace=True)
        print("Missing values dropped.")

    def filter_english_songs(self):
        """ Keep only English songs based on language fields. """
        self.data = self.data[
            (self.data['language_cld3'] == 'en') & (self.data['language_ft'] == 'en')
        ]
        print("English songs filtered.")

    def normalize_text(self, column):
        """ Normalize text data. """
        self.data[column] = self.data[column].str.lower()
        self.data[column] = self.data[column].apply(lambda x: re.sub(r'\s+', ' ', x).strip())
        print(f"Text in column '{column}' normalized.")

    def preprocess(self):
        """ Run all preprocessing steps. """
        self.load_data()
        self.drop_missing_values()
        self.filter_english_songs()

        for column in self.columns_to_normalize:
            self.normalize_text(column)

        print("Preprocessing completed.")

    def save_clean_data(self, output_path):
        """ Save the cleaned data to a new CSV. """
        self.data.to_csv(output_path, index=False)

if __name__ == "__main__":
    file_path = DATA_FILE_PATH
    output_path = f'{DATA_DIRECTORY}cleaned_dataset_{str(uuid.uuid4())}.csv'
    preprocessor = DataPreprocessor(file_path, COLUMNS_TO_NORMALIZE)
    try:
        preprocessor.preprocess()
        preprocessor.save_clean_data(output_path)
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        sys.exit(1)