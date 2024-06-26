# Module to handle data cleaning and preprocessing

import pandas as pd
import re
import sys
import uuid
from utils import DATASET_FILE_PATH, DATA_DIRECTORY

# Data columns
COLUMNS_TO_NORMALIZE = ['title', 'artist', 'lyrics', 'features', 'tag']

class DataPreprocessor:
    """
    Remove rows with missing values.
    Normalize text fields:
        Conversion to lowercase
        Elimination of extra spaces
    """
    def __init__(self, file_path, columns_to_normalize):
        self.file_path = file_path
        self.columns_to_normalize = columns_to_normalize
        self.data = None

    def load_data(self):
        """ Load data from a CSV file. """
        print("Start data load.")
        self.data = pd.read_csv(self.file_path)
        print("Data loaded successfully.")

    def drop_missing_values(self):
        """ Remove rows with missing values. """
        self.data.dropna(inplace=True)
        print("Missing values dropped.")

    def drop_same_id(self):
        """ Remove rows with duplicate 'id' column values. """
        initial_count = len(self.data)
        self.data = self.data.drop_duplicates(subset='id', keep='first')
        final_count = len(self.data)
        drops = initial_count - final_count
        print(f"Duplicates IDs dropped: {drops}")

    def filter_english_songs(self):
        """ Keep only English songs based on language fields. """
        self.data = self.data[
            (self.data['language_cld3'] == 'en') & (self.data['language_ft'] == 'en')
        ]
        print("English songs filtered.")

    def normalize_text(self, column):
        """ Normalize text data. """

        def clean_text(text):
            # remove bracketed sections like [Hook] or [Verse]
            text = re.sub(r"\[.*?\]", '', text)

            # convert to lowercase
            text = text.lower()

            # collapse multiple consecutive newline characters into a single newline
            text = re.sub(r"\n+", '\n', text)

            # remove any non-alphanumeric characters (keeping spaces, basic punctuation, and newlines)
            text = re.sub(r"[^a-zA-Z0-9 ,.!?'\n\"]", ' ', text)

            # remove any extra spaces
            text = re.sub(r'[^\S\n]+', ' ', text).strip()

            #TODO verify the need
            # text = re.sub(r"\n", ' [BRK] ', text)

            return text

        self.data[column] = self.data[column].apply(clean_text)
        print(f"Text in column '{column}' normalized.")

    def preprocess(self):
        """ Run all preprocessing steps. """
        self.load_data()
        self.drop_missing_values()
        self.drop_same_id()
        self.filter_english_songs()

        for column in self.columns_to_normalize:
            self.normalize_text(column)

        print("Preprocessing completed.")

    def save_clean_data(self, output_path):
        """ Save the cleaned data to a new CSV. """
        self.data.to_csv(output_path, index=False)
        print(f"Data saved to: '{output_path}'.")

if __name__ == "__main__":
    file_path = DATASET_FILE_PATH
    output_path = f'{DATA_DIRECTORY}cleaned_dataset_{str(uuid.uuid4())}.csv'
    preprocessor = DataPreprocessor(file_path, COLUMNS_TO_NORMALIZE)
    try:
        preprocessor.preprocess()
        preprocessor.save_clean_data(output_path)
    except Exception as e:
        print(f"An error occurred during processing: {e}")
        sys.exit(1)
