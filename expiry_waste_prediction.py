import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the inventory dataset
data = pd.read_csv("inventory_data.csv")

# Select features
features = [
    "Current_Stock",
    "Daily_Sales",
    "Days_to_Expiry",
    "Product_Age",
    "Promotion",
    "Demand_Variability"
]

X = data[features]
y = data["Expiry_Risk"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42, max_depth=3)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("Expiry / Waste Risk Prediction")
print("--------------------------------")
print("Model: Decision Tree Classifier")
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Example prediction
new_product = [[500, 70, 4, 2, 0, 15]]
risk = model.predict(new_product)

if risk[0] == 1:
    print("\nPrediction: HIGH expiry/waste risk")
else:
    print("\nPrediction: LOW expiry/waste risk")
