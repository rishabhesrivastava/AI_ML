# Viva Presentation - Intelligent Book Recommendation System

Student ID: 2025AIML049

## Introduction

I built an intelligent book recommendation system that uses text mining and machine learning to recommend books based on their content similarity.

## Problem

Online bookstores have thousands of books, making it difficult for users to discover books they might like. Traditional keyword search doesn't find semantically similar content.

## Solution

I used content-based filtering with TF-IDF vectorization and cosine similarity to recommend books based on their descriptions and genres.

## Dataset

- Goodreads Books Dataset with 20,069 books
- After cleaning: 16,091 books with descriptions
- Features: title, author, description, genres, ratings

## Methodology

1. Data preprocessing: handled missing values, removed duplicates
2. Text mining: lowercase, removed special characters, tokenization, stopword removal
3. Feature extraction: TF-IDF with 5000 features
4. Recommendation: cosine similarity to find similar books
5. UI: Streamlit web application

## Technology Stack

- Python 3.13
- pandas, numpy, scikit-learn
- matplotlib, seaborn
- streamlit
- joblib

## Results

- Response time: < 1 second
- Relevant genre-consistent recommendations
- Clean and user-friendly interface

## Challenges Faced

- NLTK SSL errors: solved by using sklearn's built-in stopwords
- Memory constraints: used sparse matrices and sequential execution
- UI text visibility: added CSS to force visible text

## Conclusion

Successfully implemented a complete book recommendation system with all requirements met. Ready for submission.

## Q&A

Questions?
