Assignment 2 — Sentiment Analysis and Topic Modelling

Total Marks: 12

NOTE:

ALL THE QUESTIONS ARE MANDATORY

·        You may use any library or framework wherever required EXCEPT for the Naive Bayes classifier (Part A, Q2), which you must implement from scratch.

·        Merge all your problems into a single Python Notebook and upload a single Python notebook (.ipynb).

·        Solutions should be placed one after the other in the submission notebook.

·        Explicitly mention each question as a Markdown cell in your notebook to segregate the different parts that you are attempting.

·        Do not submit Zip files and do not upload the dataset as part of the submission. Avoid printing irrelevant cells — marks will be deducted for very long notebooks.

·        No deadline extension will be entertained. Start early.

Dataset
Sentiment Labelled Sentences dataset (UCI Machine Learning Repository).

The dataset contains 3,000 review sentences collected from three websites — amazon.com (product reviews), yelp.com (restaurant reviews) and imdb.com (movie reviews) — with 500 positive and 500 negative sentences from each. It is provided to you as a single file, sentiment_sentences.csv, with three columns:

·        text — the review sentence.

·        sentiment — 1 for positive, 0 for negative.

·        source — amazon, yelp or imdb (the review domain).

Treat each sentence as a separate document. Place sentiment_sentences.csv in the same folder as your notebook and load it with pandas.

Source: https://archive.ics.uci.edu/dataset/331/sentiment+labelled+sentences

Citation: D. Kotzias, M. Denil, N. de Freitas, P. Smyth. “From Group to Individual Labels using Deep Features”, KDD 2015.

Part A — Sentiment Analysis
Based on Lecture 4 (Sentiment Analysis): text preprocessing and the Multinomial Naive Bayes classifier with Laplace (add-1) smoothing. This is document-level sentiment classification (positive vs negative).

1.      Load and Preprocess: Load sentiment_sentences.csv using pandas. Preprocess the text column — convert to lower case, remove punctuation and special characters, tokenize, and remove stop words. Print the cleaned tokens for one sample review.  (2 Marks)

2.      Naive Bayes from scratch + Evaluation: Split the data into training (80%) and test (20%) sets using a stratified split. Implement the Multinomial Naive Bayes classifier from scratch — compute the class priors P(c) = N_c / N and the word likelihoods with Laplace (add-1) smoothing: P(w|c) = (count(w,c) + 1) / (sum of counts in c + |V|). Predict the sentiment of the test set and report the Accuracy and the F1-score. You must NOT use a library classifier for this step.  (5 Marks)

Part B — Topic Modelling with LDA
Based on Lecture 3 (Topic Modelling and Latent Dirichlet Allocation). LDA is an unsupervised technique: each topic is a distribution over the vocabulary and each document is a mixture of topics. (For Part B, use the text column only — the sentiment and source labels are NOT given to LDA.)

3.      Document-Term Matrix, LDA and Topic Words: Build the document-term (word-count) matrix from the review sentences after removing English stop words (you may use CountVectorizer). Apply the LDA algorithm to create K = 3 topics, then list the top 10 highest-probability words in each topic. Note: you may ignore the case where some words in a topic are not highly related — LDA assigns no labels.  (3 Marks)

4.      Document-Topic Distribution: For at least 5 documents, print the distribution over the 3 topics and the dominant (most probable) topic. Optionally, compare the dominant topic against the source column to see how the discovered topics relate to the three review domains.  (2 Marks)

 

Deadline extension will not be considered. Do not submit Zip files. Do not upload the dataset as part of your submission.

For any doubts and queries, you can write to: murtuza.dahodwala@wilp.bits-pilani.ac.in

sentiment_sentences.csvsentiment_sentences.csv