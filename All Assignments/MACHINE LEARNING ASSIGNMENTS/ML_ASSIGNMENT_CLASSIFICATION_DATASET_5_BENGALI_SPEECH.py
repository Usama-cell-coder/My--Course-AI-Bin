# ===========================================
# Import Libraries
# ===========================================

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

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

train_df = pd.read_csv(r"D:\ML_ASSIGNMENT_CLASSIFICATION_DATASETS\Bengali_hate_speech_dataset\train.csv")
test_df = pd.read_csv(r"D:\ML_ASSIGNMENT_CLASSIFICATION_DATASETS\Bengali_hate_speech_dataset\test.csv")
valid_df = pd.read_csv(r"D:\ML_ASSIGNMENT_CLASSIFICATION_DATASETS\Bengali_hate_speech_dataset\validate.csv")

print("Train Shape:", train_df.shape)
print("Validation Shape:", valid_df.shape)
print("Test Shape:", test_df.shape)

print("\nMissing Values (Train)")
print(train_df.isnull().sum())

# ===========================================
# Remove Missing Values
# ===========================================

train_df.dropna(inplace=True)
valid_df.dropna(inplace=True)
test_df.dropna(inplace=True)

# ===========================================
# TF-IDF Feature Extraction
# ===========================================

tfidf = TfidfVectorizer(max_features=5000)

X_train = tfidf.fit_transform(train_df["text"])

X_valid = tfidf.transform(valid_df["text"])

X_test = tfidf.transform(test_df["text"])

y_train = train_df["label"]
y_valid = valid_df["label"]
y_test = test_df["label"]

print("\nClass Distribution")
print(y_train.value_counts())

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

rf = RandomForestClassifier(n_estimators=100, random_state=42)

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