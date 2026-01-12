import pandas as pd

data_description = {
    "Attribute": [
        "Workout_Minutes",
        "Protein_Intake",
        "Calories_Intake",
        "Sleep_Hours",
        "Training_Consistency",
        "Muscle_Gain"
    ],
    "Description": [
        "Daily exercise duration (minutes)",
        "Daily protein intake (grams)",
        "Daily calorie consumption",
        "Average sleep duration (hours)",
        "Training regularity score (1–6)",
        "Target variable (0 = No, 1 = Yes)"
    ]
}

df = pd.DataFrame(data_description)
df.to_csv("../data/dataset_description_table.csv", index=False)
print(df)