
from sklearn.tree import DecisionTreeClassifier
import joblib

#training data
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

model = DecisionTreeClassifier()
model.fit(X, y)

#save model
joblib.dump(model, "course_recommender.joblib")
print("Model saved as 'course_recommender.joblib'")
