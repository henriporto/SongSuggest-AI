import sys

DATASET_FILE_PATH = '../data/song_lyrics.csv'
DATA_DIRECTORY = '../data/'
MODEL_OUTPUT_PATH = '../models/lyricsmodel'
MODEL_LOG_OUTPUT_PATH = '../models/lyricsmodel/logs'
CLEANED_DATASET_PATH = '../data/cleaned_dataset_e7132cc2-add2-44d1-a39e-b5c38e877708.csv'
SEED = 23
MODEL_NAME = 'allenai/longformer-base-4096'

def continue_question():
    if input("Continue? s/n").lower() == "n":
        sys.exit(1)
