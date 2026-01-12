✅ Python Code File: dataset_table.py
import pandas as pd

# Create dataset description table
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

# Convert to DataFrame
df = pd.DataFrame(data_description)

# Display table
print("\nDataset Feature Description Table:\n")
print(df)

# Save table to CSV (optional)
df.to_csv("dataset_description_table.csv", index=False)

print("\nTable saved as 'dataset_description_table.csv'")