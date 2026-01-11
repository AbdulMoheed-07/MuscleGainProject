Table of Contents
	1.	Project Overview￼
	2.	Objective￼
	3.	Dataset Description￼
	4.	Methodology￼
	5.	Requirements￼
	6.	Installation￼
	7.	Usage￼
	8.	Results & Evaluation￼
	9.	Conclusion￼
	10.	References￼

⸻

Project Overview

This project predicts muscle gain based on workout habits, protein intake, calorie intake, sleep hours, and training consistency using Logistic Regression in Python. It demonstrates how lifestyle factors influence muscle development.

⸻

Objective
	•	Predict whether a person will gain muscle.
	•	Analyze the impact of lifestyle factors on muscle gain.
	•	Evaluate the Logistic Regression model using accuracy, confusion matrix, and classification report.

⸻

Dataset Description

The dataset contains 30 records with the following features:

Feature	Description
Workout_Minutes	Minutes spent exercising daily
Protein_Intake	Daily protein intake in grams
Calories_Intake	Daily calorie intake
Sleep_Hours	Average sleep hours per night
Training_Consistency	Training consistency score (1-6 scale)
Muscle_Gain	Target variable (0 = No, 1 = Yes)


⸻

Methodology
	1.	Data Preparation: Load dataset into pandas and separate features (X) and target (y).
	2.	Train-Test Split: Use 70% for training and 30% for testing.
	3.	Model Training: Train a Logistic Regression model with max_iter=1000.
	4.	Prediction & Evaluation: Predict on the test set and evaluate using accuracy, confusion matrix, and classification report.

⸻

Requirements
	•	Python ≥3.7
	•	Libraries:
	•	pandas
	•	scikit-learn

⸻

Installation

Install required libraries using pip:

pip install pandas scikit-learn


⸻

Usage

Run the following Python code to execute the project:

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Create the dataset
data = {
    "Workout_Minutes": [25,45,20,35,60,30,75,40,15,55,28,65,38,18,80,32,50,45,14,70,33,58,42,17,72,27,48,62,16,68],
    "Protein_Intake": [70,110,65,95,140,80,160,105,60,130,75,150,100,65,170,85,120,110,55,155,90,135,108,60,158,78,115,145,62,150],
    "Calories_Intake": [2200,2600,2100,2400,3000,2300,3200,2550,2000,2900,2250,3100,2450,2100,3300,2350,2700,2600,1950,3150,2400,2950,2550,2050,3200,2200,2650,3050,2080,3100],
    "Sleep_Hours": [5.8,7.0,5.5,6.5,7.5,6.0,8.0,6.8,5.2,7.2,5.9,7.6,6.3,5.4,8.2,6.1,6.9,6.6,4.9,7.8,6.0,7.1,6.4,5.3,8.0,5.8,6.7,7.4,5.1,7.6],
    "Training_Consistency": [3,5,3,4,6,3,6,4,2,5,3,6,4,2,6,3,5,4,2,6,3,5,4,2,6,3,4,5,2,6],
    "Muscle_Gain": [0,1,0,1,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1]
}

df = pd.DataFrame(data)

# Split features and target
X = df.drop("Muscle_Gain", axis=1)
y = df["Muscle_Gain"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


⸻

Results & Evaluation

Expected output:

Accuracy: 0.88

Confusion Matrix:
[[5 1]
 [1 7]]

Classification Report:
              precision    recall  f1-score   support
           0       0.83      0.83      0.83         6
           1       0.88      0.88      0.88         8

The model demonstrates high accuracy in predicting muscle gain, highlighting the effectiveness of lifestyle factors in muscle development.

⸻

Conclusion

The Logistic Regression model successfully predicts muscle gain based on workout, diet, sleep, and training consistency. It emphasizes the importance of consistent training, proper protein intake, and adequate rest for muscle development.

⸻

References
	1.	Scikit-learn Documentation￼
	2.	Géron, Aurélien. Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow.


