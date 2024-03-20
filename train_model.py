# Filename: train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'iris_model.pkl')
