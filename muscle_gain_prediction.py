import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

data = {
    "Workout_Minutes": [25,45,20,35,60,30,75,40,15,55,28,65,38,18,80,32,50,45,14,70,33,58,42,17,72,27,48,62,16,68],
    "Protein_Intake": [70,110,65,95,140,80,160,105,60,130,75,150,100,65,170,85,120,110,55,155,90,135,108,60,158,78,115,145,62,150],
    "Calories_Intake": [2200,2600,2100,2400,3000,2300,3200,2550,2000,2900,2250,3100,2450,2100,3300,2350,2700,2600,1950,3150,2400,2950,2550,2050,3200,2200,2650,3050,2080,3100],
    "Sleep_Hours": [5.8,7.0,5.5,6.5,7.5,6.0,8.0,6.8,5.2,7.2,5.9,7.6,6.3,5.4,8.2,6.1,6.9,6.6,4.9,7.8,6.0,7.1,6.4,5.3,8.0,5.8,6.7,7.4,5.1,7.6],
    "Training_Consistency": [3,5,3,4,6,3,6,4,2,5,3,6,4,2,6,3,5,4,2,6,3,5,4,2,6,3,4,5,2,6],
    "Muscle_Gain": [0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1]
}

df = pd.DataFrame(data)
X = df.drop("Muscle_Gain", axis=1)
y = df["Muscle_Gain"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))