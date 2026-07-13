# ===========================================
# Import Libraries
# ===========================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

# ===========================================
# Load Dataset
# ===========================================

df = pd.read_csv(r"D:\ML_ASSIGNMENT_CLASSIFICATION_DATASETS\Recipe Reviews and User Feedback Dataset.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

# ===========================================
# Encode Categorical Columns
# ===========================================

le = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col])

# ===========================================
# Select Features and Target
# Replace TargetColumn with your target column
# ===========================================

X = df.drop("TargetColumn", axis=1)
y = df["TargetColumn"]

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
print("Precision:", precision_score(y_test, pred_lr, average='weighted'))
print("Recall   :", recall_score(y_test, pred_lr, average='weighted'))
print("F1 Score :", f1_score(y_test, pred_lr, average='weighted'))

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
print("Precision:", precision_score(y_test, pred_rf, average='weighted'))
print("Recall   :", recall_score(y_test, pred_rf, average='weighted'))
print("F1 Score :", f1_score(y_test, pred_rf, average='weighted'))

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

print("\nModel Comparison")
print(comparison)

best_model = comparison.loc[comparison["Accuracy"].idxmax(), "Model"]

print("\nBest Performing Model:", best_model)