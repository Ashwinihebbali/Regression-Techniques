import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from data_loader import load_data

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load data
X, y = load_data("data/dataset.csv")

# Predictions
y_pred = model.predict(X)

# Metrics
print("📊 Evaluation Results")
print("MAE:", mean_absolute_error(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
print("R2 Score:", r2_score(y, y_pred))

# New prediction
hours = [[7.5]]
print(f"Predicted Marks for 7.5 hours: {model.predict(hours)[0]:.2f}")
