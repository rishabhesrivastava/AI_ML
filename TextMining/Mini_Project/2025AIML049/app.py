"""
Intelligent Book Recommendation System - Streamlit UI
Approach 1: Separate Streamlit Application
Student ID: 2025AIML049
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle

# Set page configuration for the Streamlit app
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, clean styling
st.markdown("""
<style>
    /* Light background color */
    .stApp {
        background-color: #f0f4f8;
    }
    
    /* Force all text to be visible (black by default) */
    * {
        color: #000000 !important;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        background-color: #f0f4f8;
    }
    
    /* Title styling */
    .main-title {
        font-size: 2.2rem;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 700;
        padding: 1rem;
    }
    
    /* Selected book section */
    .selected-book-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 4px solid #2563eb;
    }
    
    .selected-book-container h3 {
        color: #1e40af !important;
    }
    
    .selected-book-container p {
        color: #000000 !important;
    }
    
    .selected-book-container strong {
        color: #000000 !important;
    }
    
    /* Recommendation card styling */
    .rec-card {
        background: white;
        padding: 1.2rem;
        border-radius: 10px;
        margin: 0.8rem 0;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    
    .rec-card:hover {
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    
    .rec-title {
        color: #1e40af !important;
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .rec-info {
        color: #000000 !important;
        font-size: 0.9rem;
        margin: 0.2rem 0;
    }
    
    .rec-info strong {
        color: #000000 !important;
    }
    
    .similarity-badge {
        display: inline-block;
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white !important;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    /* Metric styling - force visibility */
    [data-testid="stMetric"] {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 8px;
    }
    
    [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: 600;
    }
    
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: 700;
        font-size: 1.5rem;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f0f4f8 0%, #e2e8f0 100%);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #f1f5f9;
        border-radius: 8px;
        padding: 0.8rem;
        font-weight: 600;
        color: #000000 !important;
    }
    
    /* Headers - black by default */
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }
    
    /* Paragraphs */
    p {
        color: #000000 !important;
    }
    
    /* Strong/bold text */
    strong {
        color: #000000 !important;
    }
    
    /* White heading class for specific headings */
    .white-heading {
        color: #ffffff !important;
    }
    
    /* Sidebar labels - white text */
    .stTextInput label, .stSelectbox label, .stSlider label {
        color: #ffffff !important;
    }
    
    /* Sidebar input text - white */
    .stTextInput input, .stSelectbox select {
        color: #ffffff !important;
    }
    
    /* Expander content - white text */
    .streamlit-expanderContent {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Header with gradient
st.markdown("""
<div style='text-align: center; padding: 1rem; margin-bottom: 1rem;'>
    <h1 style='font-size: 2.5rem; color: #ffffff; margin: 0;'>📚 Book Recommendation System</h1>
    <p style='color: #ffffff; margin: 0.5rem 0 0 0;'>Discover your next favorite book using AI-powered recommendations</p>
</div>
""", unsafe_allow_html=True)

# Load models and data with caching to improve performance
@st.cache_resource
def load_data():
    """Load the pre-trained models and dataset from disk."""
    try:
        # Load the cleaned dataset
        df = pd.read_csv('cleaned_books.csv')
        
        # Load the TF-IDF vectorizer that was trained in the notebook
        tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
        
        # Load the pre-computed cosine similarity matrix
        cosine_sim = joblib.load('cosine_similarity_matrix.pkl')
        
        # Load the list of book titles for the search dropdown
        with open('book_titles.pkl', 'rb') as f:
            book_titles = pickle.load(f)
        
        return df, tfidf_vectorizer, cosine_sim, book_titles
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None, None

# Load data
with st.spinner("📚 Loading data and models..."):
    df, tfidf_vectorizer, cosine_sim, book_titles = load_data()

if df is not None:
    # Create a reverse mapping from book title to index for quick lookup
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    
    # Sidebar for search functionality
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🔍 <span class='white-heading'>Search Books</span>", unsafe_allow_html=True)
    
    # Search box with placeholder text
    search_query = st.sidebar.text_input("📝 Enter book title:", placeholder="Type to search...")
    
    # Autocomplete suggestions based on search query
    if search_query:
        # Find books that match the search query (case-insensitive)
        matches = [title for title in book_titles if search_query.lower() in title.lower()]
        if matches:
            selected_book = st.sidebar.selectbox("📚 Select a book:", matches)
        else:
            st.sidebar.warning("❌ No matching books found.")
            selected_book = None
    else:
        # Show popular books if no search query
        selected_book = st.sidebar.selectbox("📚 Or select from popular books:", 
                                              book_titles[:50] if len(book_titles) > 50 else book_titles)
    
    st.sidebar.markdown("---")
    # Slider to select number of recommendations
    top_n = st.sidebar.slider("📊 Number of recommendations:", 5, 15, 5)
    
    # Main content area for displaying recommendations
    if selected_book:
        st.markdown(f"### 🎯 <span class='white-heading'>Recommendations for:</span> *{selected_book}*", unsafe_allow_html=True)
        
        # Get book details from the dataset
        if selected_book in indices:
            book_idx = indices[selected_book]
            book_info = df.iloc[book_idx]
            
            # Display selected book info in a styled container
            st.markdown(f"""
            <div class="selected-book-container">
                <h3 style="color: #1e40af; margin-top: 0;">📖 {book_info['title']}</h3>
                <p style="margin: 0.5rem 0;"><strong>Author:</strong> {book_info['author']}</p>
                <p style="margin: 0.5rem 0;"><strong>Genres:</strong> {book_info['genres']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display book metrics in a row
            col1, col2, col3 = st.columns(3)
            with col1:
                rating = book_info.get('avg_rating', 0)
                st.metric("⭐ Rating", f"{rating:.2f}" if pd.notna(rating) else "N/A")
            with col2:
                num_ratings = book_info.get('num_ratings', 0)
                st.metric("👥 Ratings", f"{num_ratings:,}" if pd.notna(num_ratings) else "N/A")
            with col3:
                pages = book_info.get('num_pages', 0)
                st.metric("📄 Pages", f"{pages}" if pd.notna(pages) else "N/A")
            
            # Show book description in an expandable section
            with st.expander("📖 Book Description"):
                st.markdown(f"<div style='color: #ffffff;'>{book_info['description'][:600]}...</div>", unsafe_allow_html=True)
            
            # Function to get recommendations based on cosine similarity
            def get_recommendations(title, cosine_sim_matrix=cosine_sim, df=df, top_n=top_n):
                """Get book recommendations based on title using cosine similarity."""
                if title not in indices:
                    return None
                
                # Get the index of the selected book
                idx = indices[title]
                # Get similarity scores for this book with all other books
                sim_scores = cosine_sim_matrix[idx]
                # Sort by similarity score in descending order and get top N (excluding the book itself)
                similar_indices = sim_scores.argsort()[::-1][1:top_n+1]
                similarity_scores = sim_scores[similar_indices]
                
                # Get the book details for the recommended books
                recommendations = df.iloc[similar_indices].copy()
                recommendations['similarity_score'] = similarity_scores
                
                return recommendations
            
            # Show loading spinner while finding recommendations
            with st.spinner("🔍 Finding recommendations..."):
                recommendations = get_recommendations(selected_book, top_n=top_n)
            
            if recommendations is not None:
                st.markdown("### 📚 <span class='white-heading'>Recommended Books</span>", unsafe_allow_html=True)
                
                # Display each recommendation in a styled card
                for i, (idx, row) in enumerate(recommendations.iterrows()):
                    st.markdown(f"""
                    <div class="rec-card">
                        <div class="rec-title">{i+1}. {row['title']}</div>
                        <div class="rec-info"><strong>Author:</strong> {row['author']}</div>
                        <div class="rec-info"><strong>Genres:</strong> {row['genres']}</div>
                        <div class="rec-info"><strong>Rating:</strong> ⭐ {row['avg_rating']:.2f} ({row['num_ratings']:,} ratings)</div>
                        <span class="similarity-badge">Similarity: {row['similarity_score']:.3f}</span>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("❌ Book not found in dataset.")
    
    # Statistics section
    with st.expander("📊 Dataset Statistics"):
        st.markdown("#### Dataset Overview")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📚 Total Books", f"{len(df):,}")
        with col2:
            st.metric("⭐ Average Rating", f"{df['avg_rating'].mean():.2f}")
        with col3:
            st.metric("🔢 Total Features", f"{tfidf_vectorizer.get_feature_names_out().shape[0]:,}")
        
        st.markdown("#### Top 10 Genres")
        genre_counts = df['genres'].str.split(',').explode().str.strip().value_counts().head(10)
        st.bar_chart(genre_counts, use_container_width=True)
    
    # About section
    with st.expander("ℹ️ About This System"):
        st.markdown("""
        <div style='color: #ffffff;'>
        #### How It Works
        1. **Text Preprocessing** - Clean and normalize book descriptions
        2. **Feature Extraction** - Convert text to TF-IDF vectors
        3. **Similarity Calculation** - Compute cosine similarity between books
        4. **Recommendations** - Find top-N most similar books
        
        #### Technical Details
        - **Algorithm:** Content-Based Filtering
        - **Similarity Metric:** Cosine Similarity
        - **Feature Extraction:** TF-IDF (Term Frequency-Inverse Document Frequency)
        - **Dataset:** Goodreads Books (16,000+ books)
        </div>
        """, unsafe_allow_html=True)
else:
    st.error("⚠️ Could not load data files")
    st.markdown("""
    ### Required Files
    Please ensure these files exist in the directory:
    - `cleaned_books.csv`
    - `tfidf_vectorizer.pkl`
    - `cosine_similarity_matrix.pkl`
    - `book_titles.pkl`
    
    💡 Run the Jupyter notebook first to generate these files.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; color: #64748b;'>
    <small>Built with ❤️ using Streamlit & Scikit-learn</small>
</div>
""", unsafe_allow_html=True)
