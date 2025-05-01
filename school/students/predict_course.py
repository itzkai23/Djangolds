from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Updated training data: [Age, Gender (0=Male, 1=Female), Interest_Category]
X = [
    [18, 0, 0],  # BSIT
    [19, 1, 1],  # BSBA
    [20, 1, 2],  # BSEd
    [21, 0, 3],  # BS Criminology
    [22, 1, 4],  # BA Political Science
    [23, 0, 5],  # BS Accountancy
    [24, 1, 6],  # BA Journalism
    [25, 0, 7],  # BS Social Work
    [20, 1, 0],  # BSIT
    [22, 0, 1],  # BSBA
]

y = [
    "BSIT",
    "BSBA",
    "BSEd",
    "BS Criminology",
    "BA Political Science",
    "BS Accountancy",
    "BA Journalism",
    "BS Social Work",
    "BSIT",
    "BSBA"
]

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Interest category mapper based on CMU offerings
def map_interests(interest_texts):
    interests = []
    for interest_text in interest_texts:
        interest_text = interest_text.lower()
        if "technology" in interest_text or "computer" in interest_text or "programming" in interest_text:
            interests.append(0)  # BSIT
        elif "business" in interest_text or "finance" in interest_text or "marketing" in interest_text:
            interests.append(1)  # BSBA
        elif "teaching" in interest_text or "education" in interest_text or "teacher" in interest_text:
            interests.append(2)  # BSEd, BEEd
        elif "crime" in interest_text or "criminology" in interest_text or "law enforcement" in interest_text:
            interests.append(3)  # BS Criminology
        elif "politics" in interest_text or "government" in interest_text or "public administration" in interest_text:
            interests.append(4)  # BA Political Science / Public Admin
        elif "accounting" in interest_text or "numbers" in interest_text or "finance" in interest_text:
            interests.append(5)  # Accountancy
        elif "journalism" in interest_text or "writing" in interest_text or "news" in interest_text:
            interests.append(6)  # BA Journalism
        elif "social work" in interest_text or "community" in interest_text or "helping" in interest_text:
            interests.append(7)  # BS Social Work
        else:
            interests.append(8)  # Other
    return interests

# Prediction function
def predict_course(age, interests, gender):
    gender_encoded = 0 if gender.lower() == "male" else 1
    interest_encoded = map_interests(interests)
    most_common_interest = max(set(interest_encoded), key=interest_encoded.count)
    features = np.array([[age, gender_encoded, most_common_interest]])
    return model.predict(features)[0]