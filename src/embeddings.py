# Module to handle the creation of embeddings from data

import torch
from transformers import LongformerModel, LongformerTokenizer
from utils import MODEL_OUTPUT_PATH, CLEANED_DATASET_PATH, MODEL_NAME
from model import create_tokenized_dataset
from pandas  import pd
import numpy as np
from datasets import Dataset


def load_dataset(dataset_path):
    df = pd.read_csv(dataset_path)
    df = df[['title', 'lyrics', 'tag', 'id']]
    return Dataset.from_pandas(df)


def extract_embeddings(model, tokenized_dataset):
    #TODO
    model.eval()
    all_embeddings = []
    all_ids = []

    for item in tokenized_dataset:
        #TODO move tensors to the same device as the model
        inputs = {k: v.to(model.device) for k, v in item.items()}

        #TODO get the model output, disable gradient calculation
        with torch.no_grad():
            outputs = model(**inputs)

        #TODO outputs[0] contains the last hidden state (embeddings)
        item_embeddings = outputs.last_hidden_state

        #TODO we could average the token embeddings to get a single vector per input
        #item_embeddings = torch.mean(item_embeddings, dim=1)

        # move embeddings to CPU and convert to numpy
        all_embeddings.append(item_embeddings.cpu().numpy())
        
         # collect ids
        all_ids.extend(item['id'])

    #TODO
    all_embeddings = np.concatenate(all_embeddings, axis=0)
    return all_embeddings, all_ids

def normalize_year_views():
    """Normalize year and views."""
    #TODO
    pass

def concatenate_to_create_feature():
    """Concatenate normalize_year_views and embeddings to form the final feature set for each song."""
    #TODO
    pass


def load_trained_model(model_path):
    model = LongformerModel.from_pretrained(model_path)
    return model


if __name__ == "__main__":
    # load lyrics dataset
    dataset = load_dataset(CLEANED_DATASET_PATH)

    # tokenize dataset
    tokenizer = LongformerTokenizer.from_pretrained(MODEL_NAME)
    tokenized_dataset = create_tokenized_dataset(dataset, tokenizer)

    # load trained model
    trained_model = load_trained_model(MODEL_OUTPUT_PATH)

    #TODO convert dataset to embeddings (we need to re-write with chunks)
    all_embeddings, all_ids = extract_embeddings(trained_model, tokenized_dataset)
    normalized_years_views = normalize_year_views(all_ids)
    final_feature = concatenate_to_create_feature(normalized_years_views)

    #TODO add final_feature as a new column in CLEANED_DATASET_PATH (using chunks)
    #chunk_size = 50000
    #clean_df = pd.read_csv(file_path, usecols=['id'], chunksize=chunk_size)
    # ...
    #clean_df.to_csv(CLEANED_DATASET_PATH, index=False)

    print(f"Embeddings added to the {CLEANED_DATASET_PATH} dataset and saved.")
