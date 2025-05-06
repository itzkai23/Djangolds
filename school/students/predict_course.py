import joblib
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Path to the trained pipeline model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "course_recommender.joblib")

# Load the full pipeline (vectorizer + classifier)
model = joblib.load(MODEL_PATH)

# Predefined interest categories and their associated keywords
INTEREST_CATEGORIES = {
    0: ["technology", "computer", "programming", "coding", "it", "software"],
    1: ["business", "finance", "marketing", "management", "entrepreneurship"],
    2: ["education", "teaching", "school", "learning", "teacher"],
    3: ["criminology", "law", "crime", "enforcement", "criminal justice"],
    4: ["politics", "government", "public administration", "policy", "election"],
    5: ["accounting", "numbers", "finance", "audit", "accountant"],
    6: ["journalism", "writing", "news", "media", "reporting"],
    7: ["social work", "community", "helping", "nonprofit", "charity"],
    8: ["art", "drawing", "design", "painting", "sculpture", "visual arts"],
}

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words="english")

def map_interest(interest_texts):
    """
    Classify interests based on the closest predefined category using cosine similarity.
    """
    # Combine the interest categories into a list of strings
    category_keywords = [" ".join(keywords) for keywords in INTEREST_CATEGORIES.values()]
    
    # Vectorize the category keywords and the input interests
    all_texts = category_keywords + [" ".join(interest_texts)]  # Adding user input interest as last
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Compute the cosine similarity between the user's input and predefined categories
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Find the index of the most similar category (highest similarity score)
    most_similar_category_index = similarities.argmax()
    
    # Return the category ID of the most similar category
    # If the similarity is below a threshold, classify as undefined (or BS Fine Arts)
    if similarities[0][most_similar_category_index] < 0.2:
        return 8  # Default to BS Fine Arts (category 8) when no clear match
    return most_similar_category_index


def predict_course(age, interests, gender):
    """
    Predict the course based on age, interests (list of strings), and gender.
    The model expects a numeric array of features.
    """
    # First, map the user's interests to the closest predefined category
    classified_interest = map_interest(interests)

    # Convert gender to a numeric value: 0 for male, 1 for female
    gender_encoded = 0 if gender.lower() == "male" else 1

    # Prepare the feature array with the numeric values (age, gender, and classified interest)
    features = np.array([[age, gender_encoded, classified_interest]])

    # Predict course using the ML pipeline
    prediction = model.predict(features)[0]

    return prediction

# For quick test
if __name__ == "__main__":
    result = predict_course(21, ["painting", "drawing", "design"], "female")
    print("Predicted course:", result)
