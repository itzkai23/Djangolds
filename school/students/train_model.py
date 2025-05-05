from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Expanded training data (X: features, y: labels)
X = [
    [18, 0, 0], [19, 1, 0], [20, 0, 0], [21, 1, 0], [22, 0, 0],  # BSIT
    [18, 1, 1], [19, 0, 1], [20, 1, 1], [21, 0, 1], [22, 1, 1],  # BSBA
    [18, 1, 2], [19, 1, 2], [20, 0, 2], [21, 0, 2], [22, 1, 2],  # BSEd
    [20, 0, 3], [21, 1, 3], [22, 0, 3], [23, 1, 3], [24, 0, 3],  # Criminology
    [20, 1, 4], [21, 0, 4], [22, 1, 4], [23, 0, 4], [24, 1, 4],  # PolSci
    [19, 0, 5], [20, 1, 5], [21, 0, 5], [22, 1, 5], [23, 0, 5],  # Accountancy
    [20, 1, 6], [21, 0, 6], [22, 1, 6], [23, 0, 6], [24, 1, 6],  # Journalism
    [21, 0, 7], [22, 1, 7], [23, 0, 7], [24, 1, 7], [25, 0, 7],  # Social Work
    [18, 1, 8], [19, 0, 8], [20, 1, 8], [21, 0, 8], [22, 1, 8],  # Others
]

y = [
    "BSIT", "BSIT", "BSIT", "BSIT", "BSIT",
    "BSBA", "BSBA", "BSBA", "BSBA", "BSBA",
    "BSEd", "BSEd", "BSEd", "BSEd", "BSEd",
    "BS Criminology", "BS Criminology", "BS Criminology", "BS Criminology", "BS Criminology",
    "BA Political Science", "BA Political Science", "BA Political Science", "BA Political Science", "BA Political Science",
    "BS Accountancy", "BS Accountancy", "BS Accountancy", "BS Accountancy", "BS Accountancy",
    "BA Journalism", "BA Journalism", "BA Journalism", "BA Journalism", "BA Journalism",
    "BS Social Work", "BS Social Work", "BS Social Work", "BS Social Work", "BS Social Work",
    "Other", "Other", "Other", "Other", "Other"
]

# Split the dataset: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict and calculate accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model
joblib.dump(model, "course_recommender.joblib")
print("Model saved as 'course_recommender.joblib'")
