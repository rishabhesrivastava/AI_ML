# Intelligent Book Recommendation System - Project Report

Student ID: 2025AIML049

## Problem Statement

Online bookstores have thousands of books, making it hard for users to discover books they might like. Traditional keyword search doesn't always find semantically similar content. I built an intelligent book recommendation system that uses text mining and machine learning to recommend books based on their descriptions, genres, and content similarity.

## What I Implemented

- Data preprocessing: Cleaned the Goodreads dataset by handling missing values, removing duplicates, and selecting relevant features
- Text mining: Converted book descriptions to lowercase, removed special characters, tokenized text, and removed stopwords
- Feature extraction: Used TF-IDF vectorization to create 5000 features from book descriptions and genres
- Recommendation engine: Implemented content-based filtering using cosine similarity to find similar books
- User interface: Built a Streamlit web application for searching books and viewing recommendations
- EDA: Created visualizations for rating distribution, genre distribution, and number of ratings

## How to Run

1. Install dependencies: pip install -r requirements.txt
2. Run the notebook: jupyter notebook 2025AIML049.ipynb (execute all cells to generate models)
3. Launch the UI: streamlit run app.py

## Conclusion

I successfully built a complete book recommendation system from data collection to deployment. The system uses content-based filtering with TF-IDF and cosine similarity to provide relevant book recommendations. The Streamlit UI allows users to search for books and see similar recommendations with similarity scores. All project requirements have been met.
