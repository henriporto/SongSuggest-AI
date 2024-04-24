# Module for model fine-tuning (setup, training, and saving)

from pandas  import pd
from datasets import Dataset
from transformers import set_seed, LongformerTokenizer, LongformerModel, LongformerConfig, Trainer, TrainingArguments
from utils import continue_question, SEED, MODEL_NAME, MODEL_OUTPUT_PATH, MODEL_LOG_OUTPUT_PATH, CLEANED_DATASET_PATH
import sys
import torch

def load_dataset(dataset_path):
    df = pd.read_csv(dataset_path)
    df = df[['title', 'lyrics', 'tag']]
    df = df.sample(frac=1).reset_index(drop=True) # Shuffle the DataFrame
    return Dataset.from_pandas(df)

def tokenize_function(examples, tokenizer):
    #TODO: review longformer special tokens
    combined_text = [f'song title: {title} genre: {genre} lyrics: {lyrics}' for title, genre, lyrics in zip(examples['title'], examples['tag'], examples['lyrics'])]
    return tokenizer(combined_text, padding="longest", truncation=True, max_length=4096, add_special_tokens=True)

def create_tokenized_dataset(dataset, tokenizer):
    return dataset.map(lambda examples: tokenize_function(examples, tokenizer), batched=True, remove_columns=['title', 'lyrics', 'tag'])

def verify_dataset(datasets):
    print("first 5 rows of tokenized_datasets:")
    for i in range(5):
        print(datasets[i])
    continue_question()

def define_model():
    return LongformerModel(LongformerConfig.from_pretrained(MODEL_NAME))

# TODO: configure params for my hardware
def train_model(model, tokenized_dataset):
    training_args = TrainingArguments(
        output_dir=MODEL_OUTPUT_PATH,
        num_train_epochs=5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=1000,
        weight_decay=0.05,
        logging_dir=MODEL_LOG_OUTPUT_PATH,
        logging_steps=50,
        save_steps=500,
        evaluation_strategy="steps",
        load_best_model_at_end=True,
        metric_for_best_model='loss',
        greater_is_better=False
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()

if __name__ == "__main__":
    if not torch.cuda.is_available():
        print("Cuda is not available.")
        sys.exit(1)
    set_seed(SEED)
    print("Seed set to:", SEED)
    dataset = load_dataset(CLEANED_DATASET_PATH)
    tokenizer = LongformerTokenizer.from_pretrained(MODEL_NAME)
    tokenized_dataset = create_tokenized_dataset(dataset, tokenizer)
    verify_dataset(tokenized_dataset)
    model = define_model()
    train_model(model, tokenized_dataset)
