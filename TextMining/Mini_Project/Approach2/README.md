# Intelligent Book Recommendation System - Approach 2

## Overview
This is Approach 2 of the Book Recommendation System implementation, which uses a **single Jupyter Notebook** with an **interactive user interface built directly into the notebook using ipywidgets**.

## Structure
- `2025AIML049.ipynb` - Complete ML pipeline with interactive UI (everything in one file)
- `requirements.txt` - Python dependencies
- `Goodreadss Books.csv` - Original dataset
- `cleaned_books.csv` - Preprocessed dataset (generated after running notebook)

## How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Jupyter Notebook
```bash
jupyter notebook 2025AIML049.ipynb
```
- Run all cells to perform data cleaning, EDA, feature extraction, and model training
- The interactive UI will appear in the last section
- Use the search box and dropdown to select books
- Click "Get Recommendations" to see similar books

## Features Implemented

### Data Preparation
- Data loading from CSV
- Missing value handling
- Duplicate removal
- Exploratory Data Analysis (EDA)

### Text Mining
- Tokenization
- Stop-word removal
- Lemmatization
- Text normalization

### Feature Engineering
- Bag of Words (BoW)
- TF-IDF Vectorization

### Recommendation Engine
- Content-Based Filtering
- Cosine Similarity
- Top-N Recommendation Generation

### Visualization
- Rating distribution
- Genre distribution
- Number of ratings distribution

### User Interface (ipywidgets)
- Book search with autocomplete
- Book selection dropdown
- Number of recommendations slider
- Interactive recommendation display
- Book details with similarity scores

## Technical Details
- **Algorithm**: Content-Based Filtering
- **Similarity Metric**: Cosine Similarity
- **Feature Extraction**: TF-IDF (5000 features)
- **Dataset**: 20,069 books from Goodreads
- **Text Processing**: NLTK for tokenization, stopword removal, lemmatization
- **UI Framework**: ipywidgets (built into Jupyter)

## Evaluation
The system was evaluated using:
- Dataset statistics (20,000+ books)
- Feature engineering metrics (5000 TF-IDF features)
- Similarity matrix analysis
- Text preprocessing effectiveness

## Advantages of This Approach
- Everything in a single notebook - compact and self-contained
- Interactive UI built directly into the notebook
- No need for separate files or external servers
- Easy to share and demonstrate
- All visualizations and outputs are saved in the notebook

## Important Note
This approach uses ipywidgets for the user interface. While it provides interactivity within the notebook, it may not satisfy the specific requirement of "Streamlit or Flask" mentioned in the instructions. For full compliance with the instructions, consider using Approach 1 or Approach 3.
