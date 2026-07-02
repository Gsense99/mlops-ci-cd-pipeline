import joblib
from sklearn.metrics import accuracy_score
import os

model = joblib.load("model.joblib")
X_test, y_test = joblib.load("test_data.joblib")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

os.makedirs("reports", exist_ok=True)

with open("reports/report.txt", "w") as f:
    f.write(f"Accuracy = {accuracy:.2f}")

print(f"Accuracy = {accuracy:.2f}")