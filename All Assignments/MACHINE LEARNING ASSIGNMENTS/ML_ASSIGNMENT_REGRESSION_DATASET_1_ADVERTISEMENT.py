# ===========================================
# Import Libraries
# ===========================================

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ===========================================
# Load Dataset
# ===========================================

df = pd.read_csv(r"D:\ML_ASSIGNMENT_REGRESSION DATASETS\advertising.csv")

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
# ===========================================

X = df.drop("Sales", axis=1)
y = df["Sales"]

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
# Decision Tree Regressor
# ===========================================

dt = DecisionTreeRegressor(random_state=42)

dt.fit(X_train, y_train)

pred_dt = dt.predict(X_test)

print("\n========== Decision Tree Regressor ==========")

print("MAE :", mean_absolute_error(y_test, pred_dt))
print("MSE :", mean_squared_error(y_test, pred_dt))
print("RMSE:", mean_squared_error(y_test, pred_dt, squared=False))
print("R2 Score:", r2_score(y_test, pred_dt))

# ===========================================
# KNN Regressor
# ===========================================

knn = KNeighborsRegressor(n_neighbors=5)

knn.fit(X_train, y_train)

pred_knn = knn.predict(X_test)

print("\n========== KNN Regressor ==========")

print("MAE :", mean_absolute_error(y_test, pred_knn))
print("MSE :", mean_squared_error(y_test, pred_knn))
print("RMSE:", mean_squared_error(y_test, pred_knn, squared=False))
print("R2 Score:", r2_score(y_test, pred_knn))

# ===========================================
# Model Comparison
# ===========================================

comparison = pd.DataFrame({
    "Model": ["Decision Tree", "KNN"],
    "R2 Score": [
        r2_score(y_test, pred_dt),
        r2_score(y_test, pred_knn)
    ]
})

print("\n========== Model Comparison ==========")
print(comparison)

best_model = comparison.loc[comparison["R2 Score"].idxmax(), "Model"]

print("\nBest Performing Model:", best_model)