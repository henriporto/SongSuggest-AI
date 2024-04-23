# SongSuggest AI

## Introduction

This project aims to generate a personalized list of song recommendations based on user preferences regarding lyrics, genre, year, views, and title. We employ fine-tuning techniques on language models, specifically targeting song lyrics to enhance the recommendation accuracy.

## Setup & Installation

1. **Create a Virtual Environment:**
Ensure that you are in the project's root directory before executing this command.
   ```bash
   python -m venv myenv
   ```

2. **Activate the Virtual Environment:**
   - **On Windows:**
     ```cmd
     myenv\Scripts\activate
     ```
   - **On Linux or macOS:**
     ```bash
     source myenv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

## Directory Structure

- `/data`: Stores datasets.
- `/models`: Contains model files.
- `/src`: Source code for the project's software components.
- `/tests`: Test scripts and test data.
- `/docs`: Documentation.

## Collaboration Guide

To contribute to the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone [repository-url]
   ```

2. **Navigate to the Main Branch:**
   ```bash
   git checkout main
   ```

3. **Update Local Repository:**
   ```bash
   git pull
   ```

4. **Create a New Branch:**
   Replace `{type}` with `feat` for new features or `fix` for bug fixes, and `{name}` with a brief name describing your work.
   ```bash
   git checkout -b {type}/{name}
   ```

5. **Add Changes:**
   After making your changes, add them to the staging area.
   ```bash
   git add .
   ```

6. **Commit Changes:**
   ```bash
   git commit -m "{type}: description of your changes"
   ```

7. **Push Changes:**
   Push your branch to the remote repository, setting it as the upstream branch.
   ```bash
   git push --set-upstream origin {type}/{name}
   ```

## Project Workflow

### Dataset

We utilize the [Genius Song Lyrics Dataset](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information)

### Model Fine-Tuning

Fine-tune a `bert-base-uncased` model on English song lyrics to develop `lyricsModel`. We use conditional checks on the `language_cld3` and `language_ft` fields to filter songs in English for accuracy.

### Feature Engineering

Generate embeddings for textual data and normalize numerical data:
- **Textual Embeddings**: Generate from `title + lyrics` using `lyricsModel`.
- **Tag Embeddings**: Generate using `bert-base-uncased`.
- **Numerical Features**: Normalize `year` and `views`.

Concatenate all features to form the final feature set for each song.

### Recommendation System

When users input their favorite song IDs, generate embeddings and compare them to the embeddings of all songs in the dataset using similarity metrics to identify the most similar songs.
