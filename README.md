# SongSuggest AI

## Introduction

This project aims to generate a personalized list of song recommendations based on user preferences regarding lyrics, genre, year, views, and title. We employ fine-tuning techniques on the Allenai Longformer model, specifically targeting song lyrics to enhance the recommendation accuracy.

## Project Workflow

### Dataset

We utilize the [Genius Song Lyrics Dataset](https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information)

### Model Fine-Tuning

Fine-tune [Allenai Longformer](https://huggingface.co/allenai/longformer-base-4096) model on English song lyrics to develop `lyricsModel`.

### Feature Engineering

Generate embeddings for textual data and normalize numerical data:
- **Textual Embeddings**: Generate from `title + genre + lyrics` using `lyricsModel`.
- **Numerical Features**: Normalize `year` and `views`.

Concatenate all features to form the final feature set for each song.

### Recommendation System

When users provide their favorite song IDs, we create embeddings and numerical features for these songs. We then use similarity metrics to compare these features with those of all other songs in our dataset, allowing us to identify the songs that are most similar.

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

- `/data`: Stores datasets and scripts.
- `/models`: Contains model files.
- `/src`: Source code.
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
