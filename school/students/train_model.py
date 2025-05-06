from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from faker import Faker
import random
from predict_course import map_interests  # Import the real function used in prediction

fake = Faker()

# Keywords for each interest category, aligned with map_interests()
interest_phrases = {
    0: ["technology", "computer", "programming"],
    1: ["business", "finance", "marketing"],
    2: ["teaching", "education", "teacher"],
    3: ["crime", "criminology", "law enforcement"],
    4: ["politics", "government", "public administration"],
    5: ["accounting", "numbers"],
    6: ["journalism", "writing", "news"],
    7: ["social work", "community", "helping"],
    8: ["drawing", "painting", "art", "sculpture", "design", "visual arts"]  # BS Fine Arts
}

interest_to_label = {
    0: "BSIT",
    1: "BSBA",
    2: "BSEd",
    3: "BS Criminology",
    4: "BA Political Science",
    5: "BS Accountancy",
    6: "BA Journalism",
    7: "BS Social Work",
    8: "Bs Fine Arts"
}

X = []
y = []

# Generate 1000 fake records
for _ in range(1000):
    age = random.randint(17, 25)
    gender_encoded = random.randint(0, 1)  # 0 = male, 1 = female

    # Pick an interest group
    interest_code = random.choices(
        population=list(interest_to_label.keys()),
        weights=[15, 12, 10, 8, 7, 6, 6, 6, 5],
        k=1
    )[0]

    # Generate a fake interest phrase from the chosen group
    raw_interest = random.choice(interest_phrases[interest_code])

    # Use your map_interests() to get the interest_encoded
    interest_encoded = map_interests([raw_interest])[0]

    X.append([age, gender_encoded, interest_encoded])
    y.append(interest_to_label[interest_encoded])

# Split, train, test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model
joblib.dump(model, "course_recommender.joblib")
print("Model saved as 'course_recommender.joblib'")
