from sklearn.model_selection import train_test_split
from data_loader import load_data
from model import get_model

# Load data
X, y = load_data("data/dataset.csv")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = get_model()
model.fit(X_train, y_train)

print("✅ Model trained successfully")

# Save model (optional)
import pickle
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
