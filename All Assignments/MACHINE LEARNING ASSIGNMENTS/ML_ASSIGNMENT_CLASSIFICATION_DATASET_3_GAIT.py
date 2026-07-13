# ===========================================
# Import Libraries
# ===========================================

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# ===========================================
# Load Dataset
# ===========================================

df = pd.read_csv(r"D:\ML_ASSIGNMENT_CLASSIFICATION_DATASETS\gait.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

# ===========================================
# Remove Missing Values
# ===========================================

df.dropna(inplace=True)

# ===========================================
# Features and Target
# Target Column = condition
# ===========================================

X = df.drop("condition", axis=1)
y = df["condition"]

print("\nClass Distribution")
print(y.value_counts())

# ===========================================
# Train-Test Split
# ===========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ===========================================
# Logistic Regression
# ===========================================

lr = LogisticRegression(max_iter=1000)

lr.fit(X_train, y_train)

pred_lr = lr.predict(X_test)

print("\n========== Logistic Regression ==========")

print("Accuracy :", accuracy_score(y_test, pred_lr))
print("Precision:", precision_score(y_test, pred_lr, average="weighted"))
print("Recall   :", recall_score(y_test, pred_lr, average="weighted"))
print("F1 Score :", f1_score(y_test, pred_lr, average="weighted"))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred_lr))

print("\nClassification Report")
print(classification_report(y_test, pred_lr))

# ===========================================
# Random Forest Classifier
# ===========================================

rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

print("\n========== Random Forest ==========")

print("Accuracy :", accuracy_score(y_test, pred_rf))
print("Precision:", precision_score(y_test, pred_rf, average="weighted"))
print("Recall   :", recall_score(y_test, pred_rf, average="weighted"))
print("F1 Score :", f1_score(y_test, pred_rf, average="weighted"))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred_rf))

print("\nClassification Report")
print(classification_report(y_test, pred_rf))

# ===========================================
# Model Comparison
# ===========================================

comparison = pd.DataFrame({
    "Model": ["Logistic Regression", "Random Forest"],
    "Accuracy": [
        accuracy_score(y_test, pred_lr),
        accuracy_score(y_test, pred_rf)
    ]
})

print("\n========== Model Comparison ==========")
print(comparison)

best_model = comparison.loc[comparison["Accuracy"].idxmax(), "Model"]

print("\nBest Performing Model:", best_model)