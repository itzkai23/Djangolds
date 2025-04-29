from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Sample training data
# Features: [Age, Gender (0=Male, 1=Female), Interest_Category]
# Categories:
#   0 = Technology
#   1 = Business
#   2 = Health
#   3 = Art
#   4 = Engineering
#   5 = Education
#   6 = Other

X = [
    [18, 0, 0],  # BSIT
    [19, 1, 1],  # BSBA
    [21, 1, 2],  # BSN
    [20, 0, 4],  # BSECE
    [22, 1, 5],  # BSEd
    [23, 0, 6],  # General Studies
    [18, 1, 3],  # BFA
    [19, 0, 2],  # BSN
    [20, 1, 0],  # BSIT
    [22, 0, 1],  # BSBA
]

y = [
    "BSIT",
    "BSBA",
    "BSN",
    "BSECE",
    "BSEd",
    "General Studies",
    "BFA",
    "BSN",
    "BSIT",
    "BSBA"
]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Map interests into categories for multiple interests
def map_interests(interest_texts):
    interests = []
    for interest_text in interest_texts:
        interest_text = interest_text.lower()
        if "technology" in interest_text or "computer" in interest_text or "programming" in interest_text:
            interests.append(0)
        elif "business" in interest_text or "entrepreneurship" in interest_text:
            interests.append(1)
        elif "health" in interest_text or "nursing" in interest_text or "medicine" in interest_text:
            interests.append(2)
        elif "art" in interest_text or "design" in interest_text:
            interests.append(3)
        elif "engineering" in interest_text or "machines" in interest_text:
            interests.append(4)
        elif "education" in interest_text or "teaching" in interest_text:
            interests.append(5)
        else:
            interests.append(6)
    return interests

# Prediction function to handle multiple interests
def predict_course(age, interests, gender):
    gender_encoded = 0 if gender == "Male" else 1
    interest_encoded = map_interests(interests)
    
    # Handle multiple interests by selecting the most relevant one (e.g., based on frequency)
    most_common_interest = max(set(interest_encoded), key=interest_encoded.count)
    
    features = np.array([[age, gender_encoded, most_common_interest]])
    return model.predict(features)[0]

# Example of predicting for a student with multiple interests
age = 20
interests = ["Technology", "Health", "Education"]  # Multiple interests
gender = "Female"

predicted_course = predict_course(age, interests, gender)
print(f"Predicted course: {predicted_course}")
