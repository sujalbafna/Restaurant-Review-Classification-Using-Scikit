# -*- coding: utf-8 -*-
"""Restaurant-Review-Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n_e8gDfpXdxMI9OGJWeUWGRzLfSHErWn
"""

# Install necessary libraries
!pip install scikit-learn pandas numpy

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the TSV file
from google.colab import files
uploaded = files.upload()  # Upload your TSV file here

# Assuming the file is named 'reviews.tsv'
data = pd.read_csv('Restaurant_Reviews.tsv', sep='\t')

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Drop rows with missing values (if any)
data.dropna(inplace=True)

# Split the data into features and labels
X = data['Review']  # Text column
y = data['Liked']  # Sentiment column (e.g., positive/negative)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Text preprocessing and vectorization using TF-IDF
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train a classification model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

# Define a mapping for sentiment labels
sentiment_labels = {
    1: "Positive",
    0: "Negative"
}

# Predict sentiment for new reviews
def predict_review(review_text):
    """
    Predict the sentiment of a new review.
    :param review_text: str, review text to classify
    :return: tuple, predicted sentiment label and its description
    """
    # Transform the new review into TF-IDF features
    review_tfidf = tfidf.transform([review_text])
    prediction = model.predict(review_tfidf)[0]
    sentiment_description = sentiment_labels.get(prediction, "Unknown")
    return prediction, sentiment_description

# Get user input for a new review
new_review = input("Enter a review to classify its sentiment: ")
predicted_sentiment, sentiment_description = predict_review(new_review)
print(f"\nNew Review: {new_review}")
print(f"Predicted Sentiment: {predicted_sentiment} ({sentiment_description})")

# Save the model and vectorizer
import pickle
with open('random_forest_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(tfidf, vectorizer_file)

print("\nModel and vectorizer saved successfully!")