import joblib
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "course_recommender.joblib")
model = joblib.load(MODEL_PATH)

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
        elif "accounting" in interest_text or "numbers" in interest_text:
            interests.append(5)  # Accountancy
        elif "journalism" in interest_text or "writing" in interest_text or "news" in interest_text:
            interests.append(6)  # BA Journalism
        elif "social work" in interest_text or "community" in interest_text or "helping" in interest_text:
            interests.append(7)  # BS Social Work
        else:
            interests.append(8)  # Other
    return interests

def predict_course(age, interests, gender):
    gender_encoded = 0 if gender.lower() == "male" else 1
    interest_encoded = map_interests(interests)
    most_common_interest = max(set(interest_encoded), key=interest_encoded.count)
    features = np.array([[age, gender_encoded, most_common_interest]])
    return model.predict(features)[0]

#sample 
if __name__ == "__main__":
    prediction = predict_course(24, ["magic", "walking"], "female")
    print("Recommended course:", prediction)