import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Step 1: Load data
data = pd.read_csv("stress.csv")

# Step 2: Separate input and output
X = data[["age", "sleep_hours", "work_hours"]]  # inputs
y = data["stress_level"]  # output

# Step 3: Train model
model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved!")